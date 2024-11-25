using TicketHub_BackEnd.DTOs;

namespace TicketHub_BackEnd.Services
{
    public interface IUserService
    {
        Task<UserResponseDto?> GetUserById(int id);
        Task<IEnumerable<UserResponseDto>> GetAllUsers();
        Task<UserResponseDto> CreateUser(CreateUserDto dto);
        Task<UserResponseDto?> UpdateUser(int id, UpdateUserDto dto);
        Task<bool> DeleteUser(int id);
        Task<UserResponseDto?> Login(LoginDto dto);
        Task<UserResponseDto?> GetUserByEmail(string email);
    }
}