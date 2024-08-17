import pandas as pd

# Load the Excel file
file_path = '/mnt/data/hotels.xlsx'
hotels_data = pd.read_excel(file_path)

# Generate HTML table
html_table = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hotel Information Table</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }}
        
        table {{
            width: 90%;
            border-collapse: collapse;
            margin: 20px 0;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            background-color: #fff;
        }}
        
        th, td {{
            padding: 12px 15px;
            text-align: left;
        }}
        
        th {{
            background-color: #007bff;
            color: #fff;
            font-weight: bold;
            text-transform: uppercase;
        }}
        
        tr:nth-child(even) {{
            background-color: #f4f4f4;
        }}
        
        tr:hover {{
            background-color: #f1f1f1;
        }}
        
        td {{
            border-bottom: 1px solid #ddd;
        }}
    </style>
</head>
<body>

<table>
    <thead>
        <tr>
            <th>Hotel</th>
            <th>Price</th>
            <th>Avg Review</th>
            <th>Review Count</th>
        </tr>
    </thead>
    <tbody>
'''

# Append rows of data
for _, row in hotels_data.iterrows():
    html_table += f'''
        <tr>
            <td>{row['hotel']}</td>
            <td>{row['price']}</td>
            <td>{row['score']} ({row['avg review']})</td>
            <td>{row['reviews count']}</td>
        </tr>
    '''

# Close the table and HTML document
html_table += '''
    </tbody>
</table>

</body>
</html>
'''

# Write the HTML to a file
with open('/mnt/data/hotelstable.html', 'w') as file:
    file.write(html_table)

html_table
