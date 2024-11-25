namespace TicketHub_BackEnd.Services
{
    public interface IStatisticsService
    {
        Task<SalesStatisticsDto> GetSalesStatistics();
    }
}
