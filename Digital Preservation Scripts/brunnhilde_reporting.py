import os
import csv 
import pprint 



''' 
This program parses a folder of folders of brunnhilde reports to create a summary report and item level report for use 
in archival description. It assumes that you have made no customizations to the siegfried.csv file in each output folder and
that all columns are in the same order as originally output.
'''
# This program can be run on the command line or you can set base_directory to whatever directory you want and run via IDE
base_directory = input("Enter the base directory: ")
directories = os.listdir(base_directory)
# This list is output to the item summary
list_of_directory_info = [["full_dir","identifier","total_files","file_types","dates","total_file_size (in bytes)","ASpace_input_filetypes"]]
file_date_list_global = {}
file_type_list_global = {}
file_size_global = 0
errors = []
running_num_of_reports_analyzed = 0
for j in directories: 
    full_dir = (base_directory + "\\" + j)   
    try: 
        with open(full_dir + "\\siegfried.csv", newline='') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',')
            file_type_list_local = {}
            file_date_list_local = {}
            running_file_size = 0
            running_num_of_reports_analyzed += 1
            file_type_list_local_plaintext = ""
            for i in list(csvreader)[1:]: 
                running_file_size += int(i[1])
                file_size_global += int(i[1])
                if i[7] == "":
                    file_ext_index = i[0].rfind(".") + 1
                    file_extension = "File ID blank, extension is: " + i[0][file_ext_index:]
                else:
                    file_extension = i[7]
                if file_extension not in file_type_list_global.keys():
                    file_type_list_global[file_extension] = 1 
                else: 
                    file_type_list_global[file_extension] += 1 
                if file_extension not in file_type_list_local.keys():
                    file_type_list_local[file_extension] = 1 
                else: 
                    file_type_list_local[file_extension] += 1 
                if i[2][0:4] not in file_date_list_global.keys():
                    file_date_list_global[i[2][0:4]] = 1      
                else: 
                    file_date_list_global[i[2][0:4]] += 1
                if i[2][0:4] not in file_date_list_local.keys():
                    file_date_list_local[i[2][0:4]] = 1    
                else: 
                    file_date_list_local[i[2][0:4]] += 1
                num_files = sum(file_type_list_local.values())
            for k in file_type_list_local:
                if file_type_list_local_plaintext == "":
                    file_type_list_local_plaintext = file_type_list_local_plaintext + "File types include: " + k
                else:
                    file_type_list_local_plaintext = file_type_list_local_plaintext + "; " + k
            list_of_directory_info.append([full_dir,j,num_files,file_type_list_local,file_date_list_local,running_file_size,file_type_list_local_plaintext])
    except: 
        errors.append([base_directory + "\\" + j + " not analyzed. Either no siegfried.csv file is present or a siegfried.csv file is outside of the typical directory structure."])
# Printing the overall summary to the terminal
print("Analyzing " + str(running_num_of_reports_analyzed) + " brunnhilde reports from: " + base_directory + "\n")
print("Total number of files:")
print(str(sum(file_type_list_global.values()))+ " files\n")
print("Total size of all files:")
print(str(file_size_global*0.000000000931)[0:4] + " gigabytes\n")
print("Number of file types: " + str(len(file_type_list_global.keys())))
print("File types represented:")
myKeys = list(file_type_list_global.keys())
myKeys.sort()
sorted_dict_file_types = {i: file_type_list_global[i] for i in myKeys}
for i in sorted_dict_file_types: 
    print(str(i) + ": " + str(file_type_list_global[i]) + " files or " + str((file_type_list_global[i]/sum(file_type_list_global.values()) * 100))[0:4] + "% of total")
print("")
print("Date range:")
myKeys = list(file_date_list_global.keys())
myKeys.sort()
sorted_dict_dates = {i: file_date_list_global[i] for i in myKeys}
for i in sorted_dict_dates: 
    print(str(i) + ": " + str(file_date_list_global[i]) + " files or " + str((file_date_list_global[i]/sum(file_date_list_global.values()) * 100))[0:4] + "% of total")

# Saving the overall summary to the base directory
with open(base_directory + "\\summary_report.csv","w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Directory analyzed:", base_directory])
    writer.writerow(["Total brunnhilde reports analyzed: ", str(len(list_of_directory_info)-1)])
    if len(errors) > 0: 
        writer.writerow([""])
        writer.writerow(["Errors:"])
        for i in errors: 
            writer.writerow(i)
        writer.writerow([""])
    writer.writerow(["Total number of files: ", str(sum(file_type_list_global.values()))+ " files"])
    writer.writerow(["Total size of all files: ", str(file_size_global*0.000000000931)[0:4] + " gigabytes"])
    writer.writerow(["Number of file types: ", str(len(file_type_list_global.keys()))])
    writer.writerow([""])
    writer.writerow(["File types represented:"])
    for i in sorted_dict_file_types: 
        writer.writerow([str(i),str(file_type_list_global[i]) + " files", str((file_type_list_global[i]/sum(file_type_list_global.values()) * 100))[0:4] + "% of total"])
    writer.writerow([""])
    writer.writerow(["Date range:"])
    for i in sorted_dict_dates: 
        writer.writerow([str(i),str(file_date_list_global[i]) + " files",str((file_date_list_global[i]/sum(file_date_list_global.values()) * 100))[0:4] + "% of total"])
    f.close() 
print("Summary report saved to \\" + base_directory + "\\summary_report.csv")
print("Item report saved to " + base_directory + "\\item_report.csv")

# Saving the item summary to the base directory
with open(base_directory + "\\item_report.csv","w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(list_of_directory_info)




