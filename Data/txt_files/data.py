import csv

def txt_to_csv(txt_filename="Data/txt_files/city_weather_data.txt", csv_filename="Data/csv_files/city_weather_data.csv"):
    with open(txt_filename, 'r') as txt_file, open(csv_filename, 'w', newline='', encoding='utf-8') as csv_file:

        writer = csv.writer(csv_file)

        headers = ['id', 'URL', 'Feels Like', 'Wind Speed', 'Humidity', 'Dew Point', 'Visibility', 'Probability of Precipitation']
        writer.writerow(headers)
        city_data = {}

        for line in txt_file:
            line = line.strip()
            if line.startswith("id:"):
                if city_data:
                    writer.writerow([
                        city_data.get('id', ''),
                        city_data.get('URL', ''),
                        city_data.get('Feels Like', ''),
                        city_data.get('Wind Speed', ''),
                        city_data.get('Humidity', ''),
                        city_data.get('Dew Point', ''),
                        city_data.get('Visibility', ''),
                        city_data.get('Probability of Precipitation', '')
                    ])
                
                city_data = {"id": line.split(": ")[1]}
            elif line.startswith("URL:"):
                city_data["URL"] = line.split(": ")[1]
            elif line.startswith("Feels Like:"):
                city_data["Feels Like"] = line.split(": ")[1]
            elif line.startswith("Wind Speed:"):
                city_data["Wind Speed"] = line.split(": ")[1]
            elif line.startswith("Humidity:"):
                city_data["Humidity"] = line.split(": ")[1]
            elif line.startswith("Dew Point:"):
                city_data["Dew Point"] = line.split(": ")[1]
            elif line.startswith("Visibility:"):
                city_data["Visibility"] = line.split(": ")[1]
            elif line.startswith("Probability of Precipitation:"):
                city_data["Probability of Precipitation"] = line.split(": ")[1]
        if city_data:
            writer.writerow([
                city_data.get('id', ''),
                city_data.get('URL', ''),
                city_data.get('Feels Like', ''),
                city_data.get('Wind Speed', ''),
                city_data.get('Humidity', ''),
                city_data.get('Dew Point', ''),
                city_data.get('Visibility', ''),
                city_data.get('Probability of Precipitation', '')
            ])

    print(f"Successfully converted '{txt_filename}' to '{csv_filename}'")


def convert_txt_to_csv(input_filename="Data/txt_files/list_of_country.txt", output_filename="Data/csv_files/list_of_country.csv"):
    with open(input_filename, 'r') as txt_file:
        lines = txt_file.readlines()

    with open(output_filename, 'w', newline='', encoding='utf-8') as csv_file:
       
        csv_file.write("id,Country,City,Temp,Date\n")

        for line in lines:
           
            parts = line.strip().split(", ")
            if len(parts) == 5:
                
                csv_line = f"{parts[0].split(': ')[1]},{parts[1].split(': ')[1]},{parts[2].split(': ')[1]},{parts[3].split(': ')[1]},{parts[4].split(': ')[1]}\n"
                csv_file.write(csv_line)

    print(f"Converted '{input_filename}' to '{output_filename}'.")


def main():
    txt_to_csv()
    convert_txt_to_csv()

if __name__ == '__main__':
    main()
