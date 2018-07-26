nums = {'0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine', '10': 'ten', '11': 'eleven', '12': 'twelve', '13': 'thirteen', '14': 'fourteen', '15': 'fifteen', '16': 'sixteen', '17': 'seventeeen', '18': 'eighteen', '19': 'nineteen', '20': 'twenty', '30': 'thirty', '40': 'fourty', '50': 'fifty', '60': 'sixty', '70': 'seventy', '80': 'eighty', '90': 'ninety', '10000': 'ten thousand'}

def four(digit):
  return nums[digit] + " thousand "
def three(digit):
  return nums[digit] + " hundred and "
def two(digit):
  return nums[digit + '0'] + " "

def intchecker(s):
  try:
    int(s)
  except:
    return False

usernum = ""
while(intchecker(usernum) == False):
  usernum = input("Enter a number: ")
numlen = len(usernum)

if(usernum in nums):
  print(nums[usernum])
else:
  output = ''
  if(int(usernum)%100 == 0):
    if(numlen == 3):
      output += nums[usernum[0]]+' hundred'
    elif(numlen == 4):
       output += nums[usernum[0]]+' thousand'
  elif(numlen == 4):
    output += four(usernum[0]) + three(usernum[1]) + two(usernum[2]) + nums[usernum[3]]
  elif(numlen == 3):
    output += three(usernum[0]) + two(usernum[1]) + nums[usernum[2]]
  elif(numlen == 2):
    output += two(usernum[0]) + nums[usernum[1]]
  print(output)

