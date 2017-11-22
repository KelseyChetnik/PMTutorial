#!/us/bin/python

import sys
import random as rd
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

rd.seed(11171989)


## --- FUNCTIONS --- ##

def findSNPs(calls):
    """
    Select only those lines that contain SNP data
    """
    SNPs = []

    for c in calls:
        ref = c[3]
        alt = c[4]
        if len(ref) == 1 and len(alt) == 1:
            SNPs.append(c)

    return SNPs

def evalPassFilter(calls):
    cPass = []

    for c in calls:
        cFilter = c[6]
        if cFilter == 'PASS':
            cPass.append(c)

    return cPass

def evalQualFilter(calls):
    q100 = []

    for c in calls:
        qScore = c[5]
        if qScore == '100':
            q100.append(c)

    return q100

def readFile(filePath):
    with open(filePath, "r") as inFile:
        contents = []
        for rLine in inFile:
            sLine = rLine.strip('\n')
            contents.append(sLine)

    return contents

def extractData(fileContents):
    elements = []

    for con in contents:
        if con.startswith('##') == False:
            if con.startswith('#'):
                head = con.split('\t')
                header = head[:7]+head[9:]
            else:
                row = con.split('\t')
                ele = row[:7]+row[9:]
                elements.append(ele)

    return header, elements

def findIdx(data, header):
    HGPop_idx = []
    NAPop_idx = []

    for i in range(len(header)):
        if header[i].startswith('HG'):
            HGPop_idx.append(i)
        elif header[i].startswith('NA'):
            NAPop_idx.append(i)

    return HGPop_idx, NAPop_idx

def splitData(SNPdata, rd_HG, rd_NA):
    HGPop_data = []
    NAPop_data = []

    for data in SNPdata:
        row_info = data[:7]

        HG_row = []
        for i in rd_HG:
            HG_row.append(data[i])
        HGPop_data.append(row_info+HG_row)

        NA_row = []
        for j in rd_NA:
            NA_row.append(data[j])
        NAPop_data.append(row_info+NA_row)

    return HGPop_data, NAPop_data

def countGT(popData):
    GTCounts = {'0|0': [], '1|1': [], '0|1': []}
    for i in range(5):
        pos = i+7

        hom_r = 0
        hom_a = 0
        het = 0
        other = 0
        for pop in popData:
            GT = pop[pos][:3]
            if GT == '0|0':
                hom_r += 1
            elif GT == '1|1':
                hom_a += 1
            elif GT == '0|1' or GT == '1|0':
                het += 1
            else:
                other += 1
        GTCounts['0|0'].append(hom_r)
        GTCounts['1|1'].append(hom_a)
        GTCounts['0|1'].append(het)

    return GTCounts

def getDataFrame(counts, dfHeader):

    samp = []
    GT = []
    gtCount = []

    for i in range(5):
    	pos = i+7
    	samp.extend([dfHeader[pos]]*3)
    	GT.append('0|0')
    	gtCount.append(counts['0|0'][i])
    	GT.append('1|1')
    	gtCount.append(counts['1|1'][i])
    	GT.append('0|1')
    	gtCount.append(counts['0|1'][i])


    df = pd.DataFrame({
    	"sample": samp,
    	"GT": GT,
    	"count": gtCount
    })

    return df

def makePlot(df, colors):
    sb.set_palette(colors)
    plot = sb.factorplot(x='sample', y='count', hue='GT', data = df, kind='bar')
    plt.show()

    return

## --- MAIN --- ##

#get name of file and path to file from terminal
fName = sys.argv[1]

if len(sys.argv) == 3:
    path = sys.argv[2]
else:
    path = '/Users/chetnk02/Downloads/'

#get contents of file and extract elements
contents = readFile(path+fName)
header, elements = extractData(contents)

#extract SNP data only
snps = findSNPs(elements)

#filter on PASS and QUAL = 100
data_pass = evalPassFilter(snps)
data_filtered = evalQualFilter(data_pass)

#find indexes for the two populations
HG_idx, NA_idx = findIdx(data_filtered, header)

#randomly select five individuals from each population
rd_HG = rd.sample(HG_idx, 5)
rd_NA = rd.sample(NA_idx, 5)

#make headers for each data table
HG_header = header[:7]
NA_header = header[:7]

for i in rd_HG:
    HG_header.append(header[i])
for j in rd_NA:
    NA_header.append(header[j])

#split data by population and select the 5 individual samples for each
HG_data, NA_data = splitData(data_filtered, rd_HG, rd_NA)

#get genotype counts
HG_GTcount = countGT(HG_data)
NA_GTcount = countGT(NA_data)

#convert to pandas data frame
HG_df = getDataFrame(HG_GTcount, HG_header)
NA_df = getDataFrame(NA_GTcount, NA_header)

#generate plot for each
makePlot(HG_df, sb.hls_palette(10, h=0.5))
makePlot(NA_df, sb.color_palette("PiYG", 10))
