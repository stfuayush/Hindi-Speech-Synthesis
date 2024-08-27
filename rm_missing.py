import os
import csv

def remove_nonexistent_files(metadata_file, wavs_dir, output_file):
  """
  Removes lines from a CSV file if the corresponding .wav files don't exist in a subdirectory and saves the filtered data to a new file.

  Args:
      metadata_file (str): Path to the CSV file (metadata.csv).
      wavs_dir (str): Path to the subdirectory containing .wav files (wavs).
      output_file (str, optional): Path to the output file (defaults to "metadata2.csv").
  """
  with open(metadata_file, 'r', encoding='utf-8') as csvfile, \
          open(output_file, 'w', encoding='utf-8') as new_csvfile:
    reader = csv.reader(csvfile, delimiter='|')
    writer = csv.writer(new_csvfile, delimiter='|')

    for row in reader:
      wav_filename = row[0] + '.wav'  # Extract filename from first column
      wav_path = os.path.join(wavs_dir, wav_filename)

      if os.path.exists(wav_path):
        print(row)
        writer.writerow(row)  # Write the row if the file exists
      else:
        print(f"File not found: {wav_path}")  # Print a message

  print(f"Processed metadata file and removed lines for non-existent .wav files. Results saved to {output_file}.")

if __name__ == '__main__':
  output_file = 'c:\\tts\\datasets\\hindi_female_mono\\speaker1\\speaker1-2.csv'

  metadata_file = 'c:\\tts\\datasets\\hindi_female_mono\\speaker1\\speaker1.csv'
  wavs_dir = 'c:\\tts\\datasets\\hindi_female_mono\\speaker1\\wavs\\'

  remove_nonexistent_files(metadata_file, wavs_dir,output_file)