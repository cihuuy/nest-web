<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dashboard</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 0;
        }
        .dashboard-header {
            background-color: #333;
            color: #fff;
            padding: 20px;
            text-align: center;
        }
        .dashboard-container {
            max-width: 1200px;
            margin: 20px auto;
            display: flex;
            justify-content: space-between;
            flex-wrap: wrap;
        }
        .widget {
            background-color: #fff;
            border-radius: 5px;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
            padding: 20px;
            margin-bottom: 20px;
            width: calc(33.33% - 20px);
        }
        .widget h3 {
            color: #333;
            font-size: 20px;
            margin-top: 0;
        }
        .widget p {
            color: #666;
            font-size: 16px;
        }
        @media screen and (max-width: 768px) {
            .widget {
                width: calc(50% - 20px);
            }
        }
        @media screen and (max-width: 480px) {
            .widget {
                width: 100%;
            }
        }
    </style>
</head>
<body>
    <div class="dashboard-header">
        <h1>Welcome to Dashboard</h1>
    </div>
    <div class="dashboard-container">
        <div class="widget">
            <h3>Statistics</h3>
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam in sapien purus.</p>
        </div>
        <div class="widget">
            <h3>Recent Activities</h3>
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam in sapien purus.</p>
        </div>
        <div class="widget">
            <h3>Notifications</h3>
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam in sapien purus.</p>
        </div>
    </div>
</body>
</html>
