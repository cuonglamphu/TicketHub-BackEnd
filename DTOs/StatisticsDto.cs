public class SalesStatisticsDto
{
    // Daily Stats
    public DailySalesDto Today { get; set; } = new();
    public DailySalesDto Weekly { get; set; } = new();
    public DailySalesDto Monthly { get; set; } = new();
    public DailySalesDto PredictedNextMonth { get; set; } = new();

    // Forecast Stats
    public ForecastDto QuarterForecast { get; set; } = new();
    public ForecastDto YearEndTarget { get; set; } = new();
    public GrowthRateDto GrowthRate { get; set; } = new();
}

public class DailySalesDto
{
    public decimal Amount { get; set; }
    public decimal GrowthRate { get; set; }
    public int TicketsSold { get; set; }
    public int EventCount { get; set; }
}

public class ForecastDto
{
    public decimal TargetAmount { get; set; }
    public decimal CurrentProgress { get; set; }
    public decimal ProgressPercentage { get; set; }
    public decimal AmountNeeded { get; set; }
    public decimal GrowthRate { get; set; }
    public string Note { get; set; } = string.Empty;
}

public class GrowthRateDto
{
    public decimal CurrentRate { get; set; }
    public decimal TargetRate { get; set; }
    public decimal Progress { get; set; }
    public string Status { get; set; } = string.Empty;
    public decimal Change { get; set; }
}