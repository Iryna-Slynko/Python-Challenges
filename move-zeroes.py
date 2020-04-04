#Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
   
   def moveZeroes(self, nums: List[int]) -> None:
       
        counter=0
        index=0
        
        for number in nums:
            if number!=0:
                nums[index]=number
                index+=1
            else:
                counter+=1
        for i in range (counter):
            nums[index]=0
            index+=1
