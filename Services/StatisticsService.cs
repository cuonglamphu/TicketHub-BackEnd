using Microsoft.EntityFrameworkCore;
using TicketHub_BackEnd.Data;


namespace TicketHub_BackEnd.Services
{
    public class StatisticsService : IStatisticsService
    {
        private readonly AppDbContext _context;
        private readonly ILogger<StatisticsService> _logger;

        public StatisticsService(AppDbContext context, ILogger<StatisticsService> logger)
        {
            _context = context;
            _logger = logger;
        }

        public async Task<SalesStatisticsDto> GetSalesStatistics()
        {
            var today = DateTime.UtcNow.Date;
            var startOfWeek = today.AddDays(-(int)today.DayOfWeek);
            var startOfMonth = new DateTime(today.Year, today.Month, 1);
            var startOfLastMonth = startOfMonth.AddMonths(-1);

            // Calculate daily sales
            var todaySales = await CalculateDailySales(today, today.AddDays(1));
            var weeklySales = await CalculateDailySales(startOfWeek, today.AddDays(1));
            var monthlySales = await CalculateDailySales(startOfMonth, today.AddDays(1));
            var lastMonthSales = await CalculateDailySales(startOfLastMonth, startOfMonth);

            // Calculate growth rates
            var todayGrowth = CalculateGrowthRate(todaySales.Amount, await GetPreviousDaySales());
            var weeklyGrowth = CalculateGrowthRate(weeklySales.Amount, await GetPreviousWeekSales());
            var monthlyGrowth = CalculateGrowthRate(monthlySales.Amount, lastMonthSales.Amount);

            // Forecast calculations
            var quarterForecast = await CalculateQuarterForecast();
            var yearEndTarget = await CalculateYearEndTarget();
            var growthRate = await CalculateGrowthRate();

            return new SalesStatisticsDto
            {
                Today = new DailySalesDto
                {
                    Amount = todaySales.Amount,
                    GrowthRate = todayGrowth,
                    TicketsSold = todaySales.TicketsSold,
                    EventCount = todaySales.EventCount
                },
                Weekly = new DailySalesDto
                {
                    Amount = weeklySales.Amount,
                    GrowthRate = weeklyGrowth,
                    TicketsSold = weeklySales.TicketsSold,
                    EventCount = weeklySales.EventCount
                },
                Monthly = new DailySalesDto
                {
                    Amount = monthlySales.Amount,
                    GrowthRate = monthlyGrowth,
                    TicketsSold = monthlySales.TicketsSold,
                    EventCount = monthlySales.EventCount
                },
                PredictedNextMonth = CalculatePredictedNextMonth(monthlySales.Amount, monthlyGrowth),
                QuarterForecast = quarterForecast,
                YearEndTarget = yearEndTarget,
                GrowthRate = growthRate
            };
        }

        private async Task<(decimal Amount, int TicketsSold, int EventCount)> CalculateDailySales(DateTime start, DateTime end)
        {
            var sales = await _context.Sales
                .Include(s => s.Purchases)
                    .ThenInclude(p => p.Ticket)
                .Where(s => s.SaleDate >= start && s.SaleDate < end)
                .ToListAsync();

            return (
                Amount: sales.Sum(s => s.SaleTotal),
                TicketsSold: sales.Sum(s => s.Purchases.Sum(p => p.Quantity)),
                EventCount: sales.SelectMany(s => s.Purchases).Select(p => p.Ticket.EveId).Distinct().Count()
            );
        }

        private decimal CalculateGrowthRate(decimal current, decimal previous)
        {
            if (previous == 0) return 0;
            return ((current - previous) / previous) * 100;
        }

        private async Task<decimal> GetPreviousDaySales()
        {
            var yesterday = DateTime.UtcNow.Date.AddDays(-1);
            var sales = await _context.Sales
                .Where(s => s.SaleDate.Date == yesterday)
                .SumAsync(s => s.SaleTotal);
            return sales;
        }

        private async Task<decimal> GetPreviousWeekSales()
        {
            var today = DateTime.UtcNow.Date;
            var startOfLastWeek = today.AddDays(-(int)today.DayOfWeek - 7);
            var endOfLastWeek = startOfLastWeek.AddDays(7);

            var sales = await _context.Sales
                .Where(s => s.SaleDate >= startOfLastWeek && s.SaleDate < endOfLastWeek)
                .SumAsync(s => s.SaleTotal);
            return sales;
        }

        private DailySalesDto CalculatePredictedNextMonth(decimal currentMonthSales, decimal growthRate)
        {
            var predictedAmount = currentMonthSales * (1 + (growthRate / 100));
            return new DailySalesDto
            {
                Amount = Math.Round(predictedAmount, 2),
                GrowthRate = growthRate,
                TicketsSold = 0, // Predicted values
                EventCount = 0   // Predicted values
            };
        }

        private async Task<ForecastDto> CalculateQuarterForecast()
        {
            var currentQuarter = (DateTime.UtcNow.Month - 1) / 3 + 1;
            var startOfQuarter = new DateTime(DateTime.UtcNow.Year, (currentQuarter - 1) * 3 + 1, 1);
            var endOfQuarter = startOfQuarter.AddMonths(3);

            var currentSales = await _context.Sales
                .Where(s => s.SaleDate >= startOfQuarter && s.SaleDate < DateTime.UtcNow)
                .SumAsync(s => s.SaleTotal);

            var targetAmount = 120000M; // Q2 2024 target
            var progressPercentage = (currentSales / targetAmount) * 100;

            return new ForecastDto
            {
                TargetAmount = targetAmount,
                CurrentProgress = currentSales,
                ProgressPercentage = Math.Round(progressPercentage, 2)
            };
        }

        private async Task<ForecastDto> CalculateYearEndTarget()
        {
            var startOfYear = new DateTime(DateTime.UtcNow.Year, 1, 1);
            var currentSales = await _context.Sales
                .Where(s => s.SaleDate >= startOfYear)
                .SumAsync(s => s.SaleTotal);

            var targetAmount = 500000M; // Year-end target
            var progressPercentage = (currentSales / targetAmount) * 100;

            return new ForecastDto
            {
                TargetAmount = targetAmount,
                CurrentProgress = currentSales,
                ProgressPercentage = Math.Round(progressPercentage, 2),
                AmountNeeded = targetAmount - currentSales,
                GrowthRate = 8,
                Note = $"Need ${targetAmount - currentSales:N0} more to reach goal"
            };
        }

        private async Task<GrowthRateDto> CalculateGrowthRate()
        {
            var currentMonth = DateTime.UtcNow.Month;
            var startOfCurrentMonth = new DateTime(DateTime.UtcNow.Year, currentMonth, 1);
            var startOfLastMonth = startOfCurrentMonth.AddMonths(-1);

            var currentMonthSales = await _context.Sales
                .Where(s => s.SaleDate >= startOfCurrentMonth)
                .SumAsync(s => s.SaleTotal);

            var lastMonthSales = await _context.Sales
                .Where(s => s.SaleDate >= startOfLastMonth && s.SaleDate < startOfCurrentMonth)
                .SumAsync(s => s.SaleTotal);

            var currentGrowthRate = lastMonthSales == 0 ? 0 :
                ((currentMonthSales - lastMonthSales) / lastMonthSales) * 100;
            var targetGrowthRate = 12M;

            return new GrowthRateDto
            {
                CurrentRate = Math.Round(currentGrowthRate, 2),
                TargetRate = targetGrowthRate,
                Progress = 45, // Example value
                Status = "Exceeding quarterly projection",
                Change = Math.Round(currentGrowthRate - targetGrowthRate, 2)
            };
        }

        // Implement các phương thức helper khác...
    }
}