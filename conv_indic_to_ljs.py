def process_file(input_file, output_file):
  """
  Reads an input file with format ( text_id "character" ) and writes a CSV file with format text_id|character (romanized)

  Args:
      input_file (str): Path to the input file.
      output_file (str): Path to the output CSV file.
  """
  with open(input_file, 'r', encoding='utf-8') as input_f, open(output_file, 'w', encoding='utf-8') as output_f:
    # Remove leading space before iterating through lines
    for line in input_f.readlines()[1:]:  # Skip the first line (assuming header)
      # Split the line based on space and quotation marks
      parts = line.strip().split('"')

      # Extract text id and character, remove extra spaces and leading quote
      text_id = parts[0].strip()[2:]  # Remove leading bracket and space
      character = parts[1].strip()[1:]  # Remove leading quote and trailing space

      # Write to the output file with pipe delimiter and newline (without leading space)
      output_f.write(f"{text_id}|{character}|{character}\n")  # No leading space before f-string

# Specify the input and output filenames
input_file = "c:\\tts\\datasets\\hindi_female_mono\\numbers\\numbers.txt"
output_file = "c:\\tts\\datasets\\hindi_female_mono\\numbers\\numbers.csv"

# Process the files
process_file(input_file, output_file)

print(f"Successfully processed {input_file} to {output_file}")
Convert wavs to single channel, 22050hz. Save to batch file, run from wavs directory:

mkdir out
for %%a in (*.wav) do ffmpeg -i "%%a" -ar 22050 -ac 1 out/"%%a"
Remove missing file entries from LJSpeech format dataset with this:

rm_missing.py

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