{\rtf1\ansi\ansicpg1252\cocoartf2638
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 def merge_sort(unsorted_list):\
\
if len(unsorted_list) <= 1:\
\
return unsorted_list\
\
# Find the midpoint and divide the list into two\
\
middle = len(unsorted_list) // 2\
\
left_list = unsorted_list[:middle]\
\
right_list = unsorted_list[middle:]\
\
left_list = merge_sort(left_list)\
\
right_list = merge_sort(right_list)\
\
return list(merge(left_list, right_list))\
\
# Merge the sorted halves\
\
def merge(left_half,right_half):\
\
res = []\
\
while len(left_half) != 0 and len(right_half) != 0:\
\
if left_half[0] < right_half[0]:\
\
res.append(left_half[0])\
\
left_half.remove(left_half[0])\
\
else:\
\
res.append(right_half[0])\
\
right_half.remove(right_half[0])\
\
if len(left_half) == 0:\
\
res = res + right_half\
\
else:\
\
res = res + left_half\
\
return res\
\
unsorted_list = [64, 34, 25, 12, 22, 11, 90]\
\
print(merge_sort(unsorted_list))}