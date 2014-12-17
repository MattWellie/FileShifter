#Automated version of SP WMRG 407 file manipulation
import os, sys, shutil
#from subprocess import call

#Create a dictionary to store important directories
#Create lists to store file names
dir_list = {}
vcf_files = []
bam_files = []

def make_first_dirs(target_run):
    dir_list["VCF_dir"] = os.path.join(base_file_path,target_run+"_VCF")
    dir_list["VCF_dup"] = os.path.join(dir_list["VCF_dir"], str(target_run)+"_duplicate VCF")
    dir_list["VCF_run1"] = os.path.join(dir_list["VCF_dir"], "Run 1")
    dir_list["VCF_run2"] = os.path.join(dir_list["VCF_dir"], "Run 2")
    dir_list["BAM_dir"] = os.path.join(base_file_path,target_run+"_BAM")
    dir_list["BAM_coverage"] = os.path.join(dir_list["BAM_dir"], str(target_run+" coverage report")
    dir_list["neg_dir"] = os.path.join(base_file_path, "negative")
    for x in dir_list.keys():
        os.mkdir(dir_list[x])

#Bam and Bam.bai (index files) present
def identify_bams(MiSeq_file_list):
    for x in MiSeq_file_list:
        if x[-4:] == ".bam":
            bam_files.append(x)
        elif x[-4:] == ".bai":
            bam_files.append(x)
    move_bams(bam_files)

def move_bams(bam_files):
    path_to_data
    for x in bam_files: 
        shutil.move(os.path.join(path_to_data,x), os.path.join(dir_list["BAM_dir"], x))

def identify_vcfs(MiSeq_file_list):
    ''' This function should identify all non-genome .vcf files
        File name for genomic vcfs are XXX.genome.vcf '''
    for x in MiSeq_file_list:
        if x[-4:] == ".vcf":
			if x.split('.')[1] == 'vcf:
				vcf_files.append(x)
				
#Is file name storage important? 
def identify_patients(vcf_list):
    ''' This method accomplishes two things;
        1) Identifies each unique D number (keys)
        2) Stores names of all vcf files (1&2)    '''
    patients = {}
    for x in vcf_list:
        filename_components = x.split('-')
        d_number = str(filename_components[0]) + "." + str(filename_components[1])
        if patients.has_key[d_number]:
            patients[d_number].append[x]
        else:   
            #Create a list & append filename
            patients[d_number] = [x]
    return patients

def create_patient_folders(patients):
    ''' Uses the keys from the patients dictionary
        (contains the VCF file names) and uses them
        to populate the main run directory with a 
        file for each patient '''
    unique_d_numbers = patients.keys()
    for x in unique_d_numbers:
        os.mkdir(x)

def sort_vcfs(vcf_files):
    ''' Should read all VCF file names and sort into
        Run 1 or 2 based on file name 
        At this point no VCF files have been moved'''
    for x in vcf_files:
        file_name_list = x.split("_")
        new_filename = file_name_list[0][0:-2] + file_name_list[1]
        if file_name_list[0][-2:] == '-1':
            #move to 1
            shutil.move(os.path.join(path_to_data, x), os.path.join(dir_list["VCF_run1"], new_filename))
        elif file_name_list[0][-2:] == '-2':
            #move to 2
            shutil.move(os.path.join(path_to_data, x), os.path.join(dir_list["VCF_run2"], new_filename
        
#Assumes starting position is "S:\MiSeq_data\Truseq_custom_amplicon\CRUK_SMP\SMP2\"

#Program is run and targeted to a specific run number
run_number = sys.argv[1]
base_file_path = os.path.join(os.getcwd(), target_run)
MiSeq_file = os.listdir(base_file_path)[0]

#Hard coded, but consistency from MiSeq output
path_to_data = os.path.join(base_file_path, MiSeq_file, "Data", "Intensities", "Basecalls", "Alignment")
#List contents of data folder, doesn't require move
MiSeq_file_list = os.listdir(path_to_data)

make_first_dirs(run_number)
identify_bams(MiSeq_file_list)
identify_vcfs(MiSeq_file_list)
patients = identify_patients(vcf_files)
create_patient_folders(patients)
sort_vcfs(vcf_files)
