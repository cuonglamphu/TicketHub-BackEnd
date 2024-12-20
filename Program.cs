using Microsoft.EntityFrameworkCore;
using TicketHub_BackEnd.Data;
using Microsoft.OpenApi.Models;
using TicketHub_BackEnd.Services;
using System.Text.Json.Serialization;

var builder = WebApplication.CreateBuilder(args);

// Add services to the container
builder.Services.AddControllers()
    .AddJsonOptions(options =>
    {
        options.JsonSerializerOptions.ReferenceHandler = ReferenceHandler.IgnoreCycles;
    });
builder.Services.AddDbContext<AppDbContext>(options =>
    options.UseSqlServer(builder.Configuration.GetConnectionString("DefaultConnection")));
builder.Services.AddScoped<ICategoryService, CategoryService>();
builder.Services.AddScoped<IEventService, EventService>();
builder.Services.AddScoped<ITicketService, TicketService>();
builder.Services.AddScoped<ITypeService, TypeService>();
builder.Services.AddScoped<IPurchaseService, PurchaseService>();
builder.Services.AddScoped<IUserService, UserService>();
builder.Services.AddScoped<IStatisticsService, StatisticsService>();
builder.Services.AddScoped<ISaleService, SaleService>();
builder.Services.AddScoped<IFraudDetectionService, FraudDetectionService>();
// Add Swagger
builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen(c =>
{
    c.SwaggerDoc("v1", new OpenApiInfo
    {
        Title = "TicketHub API",
        Version = "v1",
        Description = "API for TicketHub application"
    });

    // Tùy chọn: Thêm cấu hình để xử lý các schema trùng tên
    c.CustomSchemaIds(type => type.FullName);
});

// Add CORS
builder.Services.AddCors(options =>
{
    options.AddPolicy("AllowAll",
        builder =>
        {
            builder
                .AllowAnyOrigin()
                .AllowAnyMethod()
                .AllowAnyHeader();
        });
});

var app = builder.Build();

if (app.Environment.IsDevelopment())
{
    app.UseSwagger();
    app.UseSwaggerUI(c =>
    {
        c.SwaggerEndpoint("/swagger/v1/swagger.json", "TicketHub API V1");
        c.RoutePrefix = string.Empty;
    });
}

app.UseHttpsRedirection();
app.UseCors("AllowAll");
app.UseAuthorization();
app.MapControllers();

app.Run();
