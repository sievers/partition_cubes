import numpy as np
import time

def find_subsum(targ,nums,inds,cur):    
    if cur==len(nums)-1:
        return None
    if np.min(np.abs(targ-nums[cur+1:]))==0:
        #print('we found a target sum.')
        ii=np.argmin(np.abs(targ-nums)) 
        inds[ii]=True
        return inds
    else:
        for i in range(cur+1,len(nums)):
            if nums[i]<targ:
                tmp=inds.copy()
                tmp[i]=True
                ans=find_subsum(targ-nums[i],nums,tmp,i)
                if not(ans is None):
                    return ans
    return None

nkids=3  #try to split up cubes between this many children
imax=100 #search up to this number.  
t1=time.time()
ndim=3 #we live in a three-dimensional world
for i in range(2,imax):
    nums=np.flip(np.arange(1,i))**ndim
    targ=np.sum(nums)//nkids
    if targ*nkids==np.sum(nums):  #if the total isn't a multiple of the # of kids, don't even bother 
        ikid=0
        isok=True
        splits=[]  #we'll use this to keep track of which numbers went to which kids
        while (ikid<nkids-1) and isok:
            ikid=ikid+1
            inds=np.zeros(len(nums),dtype='bool')
            inds[0]=True
            ans=find_subsum(targ-nums[0],nums,inds,0)
            if ans is None:
                isok=False
            else:
                splits.append(nums[ans])
                nums=nums[np.logical_not(ans)]
        if isok:
            splits.append(nums)
            print('can split ',i-1,ndim,'dimensional spheres evenly between',nkids,'kids')
            for split in splits:
                print(np.sum(split),' = sum of ',np.round(split**(1/ndim)),' to the power ',ndim)
            break
if not(isok):
    print('sadly, no partition found.  Try increasing imax.')
 
