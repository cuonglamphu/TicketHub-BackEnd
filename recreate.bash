# Xóa database
dotnet ef database drop -f

# Xóa tất cả files trong thư mục Migrations
Remove-Item -Path "Migrations\*" -Force -Recurse

# Tạo migration mới
dotnet ef migrations add InitialMigration

# Update database
dotnet ef database update