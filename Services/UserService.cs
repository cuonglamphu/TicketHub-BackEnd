using Microsoft.EntityFrameworkCore;
using TicketHub_BackEnd.Data;
using TicketHub_BackEnd.DTOs;
using TicketHub_BackEnd.Services;
using TicketHub_BackEnd.Models;
namespace TicketHub_BackEnd.Services
{
    public class UserService : IUserService
    {
        private readonly AppDbContext _context;
        private readonly ILogger<UserService> _logger;

        public UserService(AppDbContext context, ILogger<UserService> logger)
        {
            _context = context;
            _logger = logger;
        }

        public async Task<UserResponseDto> CreateUser(CreateUserDto dto)
        {
            if (dto.UserPassword != dto.ConfirmPassword)
            {
                return new UserResponseDto
                {
                    Status = "error",
                    Message = "Confirm password does not match"
                };
            }

            var existingUser = await _context.Users
                .FirstOrDefaultAsync(u => u.UserEmail == dto.UserEmail);

            if (existingUser != null)
            {
                return new UserResponseDto
                {
                    Status = "error",
                    Message = "Email is already in use"
                };
            }

            var user = new User
            {
                UserName = dto.UserName,
                FirstName = dto.FirstName,
                LastName = dto.LastName,
                UserEmail = dto.UserEmail,
                UserPassword = BCrypt.Net.BCrypt.HashPassword(dto.UserPassword),
                UserRole = "user",
                UserJoinDate = DateTime.UtcNow
            };

            _context.Users.Add(user);
            await _context.SaveChangesAsync();

            return new UserResponseDto
            {
                Status = "success",
                Message = "Registration successful. You are now logged in.",
                UserId = user.UserId,
                UserName = user.UserName,
                FirstName = user.FirstName,
                LastName = user.LastName,
                UserEmail = user.UserEmail,
                UserRole = user.UserRole,
                UserJoinDate = user.UserJoinDate,
                TotalTickets = 0,
                TotalSpent = 0
            };
        }

        public async Task<UserResponseDto?> Login(LoginDto dto)
        {
            var user = await _context.Users
                .FirstOrDefaultAsync(u => u.UserEmail == dto.UserEmail);

            if (user == null || !BCrypt.Net.BCrypt.Verify(dto.UserPassword, user.UserPassword))
            {
                return null;
            }

            return new UserResponseDto
            {
                Status = "success",
                Message = "Login successful",
                UserId = user.UserId,
                UserName = user.UserName,
                FirstName = user.FirstName,
                LastName = user.LastName,
                UserEmail = user.UserEmail,
                UserRole = user.UserRole,
                UserJoinDate = user.UserJoinDate
            };
        }

        // Implement các phương thức khác của interface
        public async Task<UserResponseDto?> GetUserById(int id)
        {
            return await _context.Users
                .Where(u => u.UserId == id)
                .Select(u => new UserResponseDto
                {
                    Status = "success",
                    Message = "User retrieved successfully",
                    UserId = u.UserId,
                    UserName = u.UserName,
                    FirstName = u.FirstName,
                    LastName = u.LastName,
                    UserEmail = u.UserEmail,
                    UserRole = u.UserRole,
                    UserJoinDate = u.UserJoinDate,
                    TotalTickets = u.Sales
                        .SelectMany(s => s.Purchases)
                        .Sum(p => p.Quantity),
                    TotalSpent = u.Sales
                        .SelectMany(s => s.Purchases)
                        .Sum(p => p.Quantity * p.Ticket.TicketPrice)
                })
                .FirstOrDefaultAsync();

        }

        public async Task<IEnumerable<UserResponseDto>> GetAllUsers()
        {
            return await _context.Users
                .Include(u => u.Sales)
                    .ThenInclude(s => s.Purchases)
                        .ThenInclude(p => p.Ticket)
                .Select(u => new UserResponseDto
                {
                    Status = "success",
                    Message = "Users retrieved successfully",
                    UserId = u.UserId,
                    UserName = u.UserName,
                    FirstName = u.FirstName,
                    LastName = u.LastName,
                    UserEmail = u.UserEmail,
                    UserRole = u.UserRole,
                    UserJoinDate = u.UserJoinDate,
                    TotalTickets = u.Sales
                        .SelectMany(s => s.Purchases)
                        .Sum(p => p.Quantity),
                    TotalSpent = u.Sales
                        .SelectMany(s => s.Purchases)
                        .Sum(p => p.Quantity * p.Ticket.TicketPrice)
                })
                .ToListAsync();
        }

        public async Task<UserResponseDto?> UpdateUser(int id, UpdateUserDto dto)
        {
            var user = await _context.Users.FindAsync(id);
            if (user == null) return null;

            user.UserName = dto.UserName;
            user.UserEmail = dto.UserEmail;
            if (!string.IsNullOrEmpty(dto.UserPassword))
            {
                user.UserPassword = BCrypt.Net.BCrypt.HashPassword(dto.UserPassword);
            }

            await _context.SaveChangesAsync();

            return new UserResponseDto
            {
                Status = "success",
                Message = "User updated successfully",
                UserId = user.UserId,
                UserName = user.UserName,
                UserEmail = user.UserEmail,
                UserRole = user.UserRole,
                UserJoinDate = user.UserJoinDate
            };
        }

        public async Task<bool> DeleteUser(int id)
        {
            var user = await _context.Users.FindAsync(id);
            if (user == null) return false;

            _context.Users.Remove(user);
            await _context.SaveChangesAsync();
            return true;
        }

        public async Task<UserResponseDto?> GetUserByEmail(string email)
        {
            var user = await _context.Users
                .FirstOrDefaultAsync(u => u.UserEmail == email);

            if (user == null) return null;

            return new UserResponseDto
            {
                Status = "success",
                Message = "User retrieved successfully",
                UserId = user.UserId,
                UserName = user.UserName,
                UserEmail = user.UserEmail,
                UserRole = user.UserRole,
                UserJoinDate = user.UserJoinDate
            };
        }
    }
}
