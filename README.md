# TicketHub-BackEnd

## How to run

### Prerequisites

-   .NET SDK
-   SQL Server

### Steps

1. Clone the repository
2. Open the terminal in the project directory
3. Change the connection string in `appsettings.json` to your SQL Server connection string (Create Database `TicketHub` is required)
4. Install the dependencies by running `dotnet restore`
5. Run `recreate.bash` to migrate and seed the database
6. Run `python import_music.py`, `python import_image.py` to seed the event data (run 1 time each file only)
7. Run `dotnet run` in the terminal

## How to use

1. Open the Swagger UI by running `https://localhost:5054` in the browser
2. Use the available endpoints to interact with the API

## Note

-   Bot creator: must be focus on `/api/Ticket/purchase` endpoint
-   Data Generator: must be focus on buying flow and more to make sure the data simulate as a real user and the data is more realistic ( Add some case illogical like buying 0 ticket, buying 1 ticket for 1000000 times, 1 ip many user, 1 ip buy many event, 1 event many user buy ( with large amount of ticket), etc... )

