import os
import csv

# Просим ввести имя файла и проверяем его расширение
print("Firefox -> Edge password converter")
filename = input("Please enter full path to exported CSV file: ")
if not filename.endswith('.csv'):
    print('Error! Wrong file extension.')
    raise SystemExit

input_file = filename
output_file = os.path.splitext(filename)[0] + '_converted.csv'


with open(input_file, 'r', newline='') as csvfile:
    # Определяем объект csv.reader
    reader = csv.reader(csvfile)
    
    # Определяем заголовки столбцов
    header = next(reader)
    num_cols = len(header)
    new_header = ['name'] + header[:3]

   
    with open(output_file, 'w', newline='') as out_file:
        writer = csv.writer(out_file)
        writer.writerow(new_header)
     
        for row in reader:
            # Извлекаем первые 3 столбца
            new_row = [row[0]] + row[:3]
            writer.writerow(new_row)

print('Successfully converted! File saved as: ' + out_file)
input("Press ENTER to exit")