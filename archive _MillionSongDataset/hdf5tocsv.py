"""
 Eric Li, Yuwei Wang, Wanqin Chen
 Northwestern University - CS396 Data Science (Team I)
 April 25 2022

 Credit to Alexis Greenstreet for inspiration for portions of code
 https://github.com/AGeoCoder/Million-Song-Dataset-HDF5-to-CSV/blob/master/msdHDF5toCSV.py
"""

import os
import glob
import hdf5_getters

## Test os.walk
# for root, dirs, files in os.walk("."):
#     dirs[:] = [d for d in dirs if d not in ("env")]
#     files = glob.glob(os.path.join(root,'*.h5'))
#     for name in files:
#         print(os.path.join(root, name))

# Write Headers to CSV File
outputFile = open("songCSV.csv", "w")
csvRowString = ("ArtistFamiliarity,ArtistHotness,ArtistID,ArtistLatitude," +
    "ArtistLongitude,ArtistLocation,ArtistName,Release,ReleaseID,SongID," +
    "SongHotness,Title,Danceability,Duration,EndOfFadeIn,Energy,Key,KeyConfidence," +
    "Loudness,Mode,ModeConfidence,StartOfFadeIn,Tempo,TimeSignature," +
    "TimeSignatureConfidence,TrackID,Year\n")
outputFile.write(csvRowString)

csvRowString = ""

## Loop through all subdirectories
for root, dirs, files in os.walk("."):
    dirs[:] = [d for d in dirs if d not in ("env")]
    files = glob.glob(os.path.join(root,'*.h5'))

    ## Loop through all relevant .h5 files in this subdirectory
    for f in files:
        ## Sample song from test file
        # f = "TRAAAAW128F429D538.h5"

        ## Open the song and pull the relevant attributes
        songFile = hdf5_getters.open_h5_file_read(f)

        artistFamiliarity = str(hdf5_getters.get_artist_familiarity(songFile))
        csvRowString += artistFamiliarity + ","

        artistHotness = str(hdf5_getters.get_artist_hotttnesss(songFile))
        csvRowString += artistHotness + ","

        artistID = str(hdf5_getters.get_artist_id(songFile))
        csvRowString += artistID + ","

        artistLatitude = str(hdf5_getters.get_artist_latitude(songFile))
        csvRowString += artistLatitude + ","

        artistLongitude = str(hdf5_getters.get_artist_longitude(songFile))
        csvRowString += artistLongitude + ","

        artistLocation = str(hdf5_getters.get_artist_location(songFile))
        csvRowString += artistLocation.replace(",","") + ","

        artistName = str(hdf5_getters.get_artist_name(songFile))
        csvRowString += artistName + ","

        release = str(hdf5_getters.get_release(songFile))
        csvRowString += release.replace(",","") + ","

        releaseID = str(hdf5_getters.get_release_7digitalid(songFile))
        csvRowString += releaseID + ","

        songID = str(hdf5_getters.get_song_id(songFile))
        csvRowString += songID + ","

        songHotness = str(hdf5_getters.get_song_hotttnesss(songFile))
        csvRowString += songHotness + ","

        title = str(hdf5_getters.get_title(songFile))
        csvRowString += title + ","

        danceability = str(hdf5_getters.get_danceability(songFile))
        csvRowString += danceability + ","

        duration = str(hdf5_getters.get_duration(songFile))
        csvRowString += duration + ","

        endOfFadeIn = str(hdf5_getters.get_end_of_fade_in(songFile))
        csvRowString += endOfFadeIn + ","

        energy = str(hdf5_getters.get_energy(songFile))
        csvRowString += energy + ","

        key = str(hdf5_getters.get_key(songFile))
        csvRowString += key + ","

        keyConfidence = str(hdf5_getters.get_key_confidence(songFile))
        csvRowString += keyConfidence + ","

        loudness = str(hdf5_getters.get_loudness(songFile))
        csvRowString += loudness + ","

        mode = str(hdf5_getters.get_mode(songFile))
        csvRowString += mode + ","

        modeConfidence = str(hdf5_getters.get_mode_confidence(songFile))
        csvRowString += modeConfidence + ","

        startOfFadeIn = str(hdf5_getters.get_start_of_fade_out(songFile))
        csvRowString += startOfFadeIn + ","

        tempo = str(hdf5_getters.get_tempo(songFile))
        csvRowString += tempo + ","

        timeSignature = str(hdf5_getters.get_time_signature(songFile))
        csvRowString += timeSignature + ","

        timeSignatureConfidence = str(hdf5_getters.get_time_signature_confidence(songFile))
        csvRowString += timeSignatureConfidence + ","

        trackID = str(hdf5_getters.get_track_id(songFile))
        csvRowString += trackID + ","

        year = str(hdf5_getters.get_year(songFile))
        csvRowString += year + "\n"

        ## Test csvRowString
        # print(csvRowString)

        ## Write Song to CSV File
        outputFile.write(csvRowString)
        csvRowString = ""

        songFile.close()

outputFile.close()