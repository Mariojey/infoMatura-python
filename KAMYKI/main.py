# N = 6
# iterator = 1
# while N>0:
#     if(iterator%2!=0):
#         if (N-4 <= 0) or (N-3 <= 0) or (N-1 <= 0):
#             print('Ada ma strategię')
#     elif(iterator%2==0):
#         if (N-4 <= 0) or (N-3 <= 0) or (N-1 <= 0):
#             print('Ada nie ma strategii')
#     iterator += 1
N = 6
isReal = 'TNTT'
iterator = 4
while iterator <= N:
    if isReal[iterator-1] == 'N' or isReal[iterator-3] == 'N' or isReal[iterator-4] == 'N':
        isReal += 'T'
    else:
        isReal += 'N'
    iterator += 1
print(isReal)