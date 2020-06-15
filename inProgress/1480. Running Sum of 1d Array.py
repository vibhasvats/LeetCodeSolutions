
def runningsum(nums):
    output = []
    sum=0
    for num in nums:
        sum += num
        output.append(sum)
    return output

if __name__ == '__main__':
    # nums= [1,2,3,4]
    # nums = [1, 1, 1, 1, 1]
    nums = [3, 1, 2, 10, 1]
    print(runningsum(nums))