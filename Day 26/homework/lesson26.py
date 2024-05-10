#დავალება 1

def num_list(nums):
    num = 0
    for i in range(0,len(nums),2): 
        num += nums[i]
    return nums
    
num0 = [0,1,2,3,4,5,6,7,8,9,10]
result = num_list(num0)
print("some of the even index: ",result)

# დავალება 2

def ox_ra_tqvi_tyeshela_oh (tyeshela):
    if tyeshela % 2 ==0 :
        return"even"
    else:
        return "odd"

amat_swavla_kiara_maimunoba_da_virishviloba_undat=int(input("please enter rizz : "))
print("youre number is :",ox_ra_tqvi_tyeshela_oh (amat_swavla_kiara_maimunoba_da_virishviloba_undat))

#დავალება 3
def num_tester (num):
    if num <= 1:
        return "false"
    if num <= 3:
        return "true"
    if num % 2 == 0 or num % 3 == 0 :
        return "not prime"
    
    
    for i in range(5,int(num**0.5)+1):
        if num % i == 0 :
            return "false"
    return "prime"

#დავალება 4

def word_tester (word):
    return [name.capitalize() for name in word]
word = ["david", "chad", "gigachad"]
print (word_tester(word))

def nums_list (nums):
    updated_nums = []
    for i in nums:
        if i % 2 == 0:
            updated_nums.append(i // 2)
        else :
            updated_nums.append(i*2)
    return updated_nums 

numlst=[1,2,3,4,5,6,7,8,9,10]
print(nums_list(numlst))