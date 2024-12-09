using Microsoft.ML.OnnxRuntime;
using Microsoft.ML.OnnxRuntime.Tensors;
using TicketHub_BackEnd.DTOs;
using TicketHub_BackEnd.Data;
using Microsoft.EntityFrameworkCore;
namespace TicketHub_BackEnd.Services
{
    public class FraudDetectionService : IFraudDetectionService
    {
        private readonly AppDbContext _context;
        private readonly InferenceSession _session;

        public FraudDetectionService(AppDbContext context)
        {
            _context = context;
            string modelPath = Path.Combine(Directory.GetCurrentDirectory(), "Services", "ML", "fraud_detection_model.onnx");

            if (!File.Exists(modelPath))
            {
                throw new FileNotFoundException($"Model file not found at {modelPath}");
            }

            Console.WriteLine($"Loading model from: {modelPath}");
            _session = new InferenceSession(modelPath);

            // In chi tiết về model
            Console.WriteLine("\nModel Input Nodes:");
            foreach (var node in _session.InputMetadata)
            {
                Console.WriteLine($"Input Name: {node.Key}");
                try
                {
                    if (node.Value.IsTensor)
                    {
                        Console.WriteLine($"Input Shape: [{string.Join(",", node.Value.Dimensions)}]");
                        Console.WriteLine($"Input Type: {node.Value.ElementType}");
                    }
                    else
                    {
                        Console.WriteLine("Input is not a tensor");
                    }
                }
                catch (Exception ex)
                {
                    Console.WriteLine($"Error processing input metadata: {ex.Message}");
                }
            }

            Console.WriteLine("\nModel Output Nodes:");
            foreach (var node in _session.OutputMetadata)
            {
                Console.WriteLine($"Output Name: {node.Key}");
                try
                {
                    if (node.Value.IsTensor)
                    {
                        Console.WriteLine($"Output Shape: [{string.Join(",", node.Value.Dimensions)}]");
                        Console.WriteLine($"Output Type: {node.Value.ElementType}");
                    }
                    else
                    {
                        Console.WriteLine("Output is not a tensor");
                    }
                }
                catch (Exception ex)
                {
                    Console.WriteLine($"Error processing output metadata: {ex.Message}");
                }
            }
        }

        public Task<bool> DetectFraud(CreatePurchaseDto purchase)
        {
            throw new NotImplementedException();
        }

        public async Task<bool> IsFraudulentAsync(int userId, CreatePurchaseDto purchase)
        {
            if (purchase == null)
            {
                throw new ArgumentNullException(nameof(purchase), "Purchase cannot be null.");
            }

            if (string.IsNullOrEmpty(purchase.IpAddress))
            {
                throw new ArgumentNullException(nameof(purchase.IpAddress), "IpAddress cannot be null or empty.");
            }

            var now = DateTime.UtcNow;

            float amount = (float)await _context.Sales
                .Where(s => s.UserId == userId && s.SaleDate.Date == now.Date)
                .SumAsync(s => s.SaleTotal);

            int currentHour = now.Hour;
            int ipCount = await _context.Sales
                .Where(s => s.UserId == userId &&
                           s.IpAddress == purchase.IpAddress &&
                           s.SaleDate.Hour == currentHour)
                .CountAsync();



            float timeHour = currentHour;

            var inputArray = new[] { amount, (float)ipCount, timeHour };
            // Query db to get all sale have same ip address and same hour
            var sales = await _context.Sales
                .Where(s => s.UserId == userId &&
                           s.IpAddress == purchase.IpAddress &&
                           s.SaleDate.Hour == currentHour)
                .ToListAsync();

            Console.WriteLine(sales);
            Console.WriteLine($"Amount: {amount}, IpCount: {ipCount}, TimeHour: {timeHour}");
            Console.WriteLine($"InputArray: [{string.Join(", ", inputArray)}]");

            var dimensions = new[] { 1, 3 };
            var inputTensor = new DenseTensor<float>(inputArray, dimensions);

            try
            {
                Console.WriteLine($"Input tensor shape: [{string.Join(",", inputTensor.Dimensions.ToArray())}]");

                var results = _session.Run(new[] { NamedOnnxValue.CreateFromTensor("input", inputTensor) });



                Console.WriteLine($"Number of outputs: {results.Count}");
                foreach (var result in results)
                {
                    Console.WriteLine($"Output name: {result.Name}");
                    Console.WriteLine($"Output type: {result.ElementType}");

                    try
                    {
                        if (result.Name == "output_label")
                        {
                            var labelTensor = result.AsTensor<long>();
                            if (labelTensor != null)
                            {
                                var label = labelTensor.ToArray()[0];
                                Console.WriteLine($"Prediction label: {label}");


                                return label == 1;
                            }
                        }
                        else if (result.Name == "output_probability")
                        {
                            try
                            {
                                // Lấy tensor dưới dạng mảng 2 chiều
                                var probabilityTensor = result.AsTensor<float>();
                                Console.WriteLine($"Probability tensor shape: [{string.Join(",", probabilityTensor.Dimensions.ToArray())}]");
                                if (probabilityTensor != null)
                                {
                                    var probArray = probabilityTensor.ToArray();
                                    float notFraudProb = probArray[0];
                                    float fraudProb = probArray[1];
                                    Console.WriteLine($"Fraud Probability: {fraudProb:P2}");
                                    Console.WriteLine($"Not Fraud Probability: {notFraudProb:P2}");
                                }
                            }
                            catch (Exception ex)
                            {
                                Console.WriteLine($"Error processing probabilities: {ex.Message}");
                            }
                        }
                    }
                    catch (Exception ex)
                    {
                        Console.WriteLine($"Error processing result: {ex.Message}");
                    }
                }

                Console.WriteLine("Could not process model output");
                return false;
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Error during fraud detection: {ex.Message}");
                Console.WriteLine($"Stack trace: {ex.StackTrace}");
                throw;
            }
        }
    }
}