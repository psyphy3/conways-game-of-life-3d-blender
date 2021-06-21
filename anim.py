import bpy

f=0;            
mats=[[[0 for i in range(10)] for j in range(10)] for k in range (10)]    
temp=[[[-1 for i in range(10)] for j in range(10)] for k in range (10)]       
           
for i in range (0,10):
    for j in range (0,10):
        for k in range (0,10):
            if (i!=0 or j!=0 or k!=0):
                bpy.data.materials['Material.'+str(i)+str(j)+str(k)].node_tree.nodes['Principled BSDF'].inputs[18].default_value=0
            if k!=0:
                mats[i][j][k-1]=bpy.data.materials['Material.'+str(i)+str(j)+str(k)].node_tree.nodes['Principled BSDF'].inputs[18]
            if k==0 and j!=0:
                mats[i][j-1][9]=bpy.data.materials['Material.'+str(i)+str(j)+str(k)].node_tree.nodes['Principled BSDF'].inputs[18]
            if k==0 and j==0 and i!=0:
                mats[i-1][9][9]=bpy.data.materials['Material.'+str(i)+str(j)+str(k)].node_tree.nodes['Principled BSDF'].inputs[18]
          
                    
bpy.data.materials['Material.1000'].node_tree.nodes['Principled BSDF'].inputs[18].default_value=0         
mats[9][9][9]=bpy.data.materials['Material.1000'].node_tree.nodes['Principled BSDF'].inputs[18]

'''   
mats[2][3][4].default_value=1
mats[2][2][4].default_value=1  
mats[3][2][4].default_value=1 
mats[4][2][4].default_value=1 
mats[5][2][3].default_value=1
mats[5][2][3].default_value=1  
mats[3][3][3].default_value=1 
mats[3][3][2].default_value=1 
mats[3][3][1].default_value=1
mats[6][7][7].default_value=1  
mats[6][7][6].default_value=1 
mats[5][7][6].default_value=1 
''' 
for i in range (0,10):
        for j in range (0,10):
            for k in range (0,10):
                mats[i][j][k].keyframe_insert(data_path='default_value',frame=300)
                
                            
for f in range (330,361,30):
    
    for i in range (0,10):
        for j in range (0,10):
            for k in range (0,10):
                if (mats[i][j][k].default_value==1):
                    n=0
                    
                    if (k!=9):
                        if (mats[i][j][k+1].default_value==1):
                            n+=1;
                    if (k!=0):
                        if (mats[i][j][k-1].default_value==1):
                            n+=1;
                    if (j!=9):
                        if (mats[i][j+1][k].default_value==1):
                            n+=1;
                    if (j!=0):
                        if (mats[i][j-1][k].default_value==1):
                            n+=1;
                    if (i!=9):
                        if (mats[i+1][j][k].default_value==1):
                            n+=1;
                    if (i!=0):
                        if (mats[i-1][j][k].default_value==1):
                            n+=1;
                            
                            
                            
                    if (j!=9 and k!=9):     
                        if (mats[i][j+1][k+1].default_value==1):
                            n+=1
                            
                    if (j!=0 and k!=0):
                        if (mats[i][j-1][k-1].default_value==1):
                            n+=1
                       
                    if (i!=9 and k!=9): 
                        if (mats[i+1][j][k+1].default_value==1):
                            n+=1
                            
                    if (i!=0 and k!=0):
                        if (mats[i-1][j][k-1].default_value==1):
                            n+=1
                        
                    if (i!=9 and j!=9):
                        if (mats[i+1][j+1][k].default_value==1):
                            n+=1
                            
                    if (i!=0 and j!=0):
                        if (mats[i-1][j-1][k].default_value==1):
                            n+=1
                            
                      
                    if (j!=9 and k!=0):  
                        if (mats[i][j+1][k-1].default_value==1):
                            n+=1
                            
                    if (j!=0 and k!=9):
                        if (mats[i][j-1][k+1].default_value==1):
                            n+=1
                            
                    if (i!=9 and k!=0):
                        if (mats[i+1][j][k-1].default_value==1):
                            n+=1
                            
                    if (i!=0 and k!=9):
                        if (mats[i-1][j][k+1].default_value==1):
                            n+=1
                            
                    if (i!=9 and j!=0):
                        if (mats[i+1][j-1][k].default_value==1):
                            n+=1
                            
                    if (i!=0 and j!=9):
                        if (mats[i-1][j+1][k].default_value==1):
                            n+=1
                            
                            
                            
                            
                    if (i!=9 and j!=9 and k!=9):       
                        if (mats[i+1][j+1][k+1].default_value==1):
                            n+=1
                        
                    if (i!=9 and j!=9 and k!=0):  
                        if (mats[i+1][j+1][k-1].default_value==1):
                            n+=1
                            
                    if (i!=9 and j!=0 and k!=9):  
                        if (mats[i+1][j-1][k+1].default_value==1):
                            n+=1
                            
                    if (i!=0 and j!=9 and k!=9):  
                        if (mats[i-1][j+1][k+1].default_value==1):
                            n+=1
                    
                    if (i!=0 and j!=0 and k!=0):  
                        if (mats[i-1][j-1][k-1].default_value==1):
                            n+=1    
                            
                    if (i!=0 and j!=0 and k!=9):  
                        if (mats[i-1][j-1][k+1].default_value==1):
                            n+=1
                            
                    if (i!=0 and j!=9 and k!=0):  
                        if (mats[i-1][j+1][k-1].default_value==1):
                            n+=1
                            
                    if (i!=9 and j!=0 and k!=0):  
                        if (mats[i+1][j-1][k-1].default_value==1):
                            n+=1
                    
                    
                            
                    if (n==4 or n==5):
                        temp[i][j][k]=1
                    else:
                        temp[i][j][k]=0
                            
                            
                            
                elif (mats[i][j][k].default_value==0):
                    n=0
                    if (k!=9):
                        if (mats[i][j][k+1].default_value==1):
                            n+=1;
                    if (k!=0):
                        if (mats[i][j][k-1].default_value==1):
                            n+=1;
                    if (j!=9):
                        if (mats[i][j+1][k].default_value==1):
                            n+=1;
                    if (j!=0):
                        if (mats[i][j-1][k].default_value==1):
                            n+=1;
                    if (i!=9):
                        if (mats[i+1][j][k].default_value==1):
                            n+=1;
                    if (i!=0):
                        if (mats[i-1][j][k].default_value==1):
                            n+=1;
                            
                            
                    if (j!=9 and k!=9):     
                        if (mats[i][j+1][k+1].default_value==1):
                            n+=1
                            
                    if (j!=0 and k!=0):
                        if (mats[i][j-1][k-1].default_value==1):
                            n+=1
                       
                    if (i!=9 and k!=9): 
                        if (mats[i+1][j][k+1].default_value==1):
                            n+=1
                            
                    if (i!=0 and k!=0):
                        if (mats[i-1][j][k-1].default_value==1):
                            n+=1
                        
                    if (i!=9 and j!=9):
                        if (mats[i+1][j+1][k].default_value==1):
                            n+=1
                            
                    if (i!=0 and j!=0):
                        if (mats[i-1][j-1][k].default_value==1):
                            n+=1
                      
                    if (j!=9 and k!=0):  
                        if (mats[i][j+1][k-1].default_value==1):
                            n+=1
                            
                    if (j!=0 and k!=9):
                        if (mats[i][j-1][k+1].default_value==1):
                            n+=1
                            
                    if (i!=9 and k!=0):
                        if (mats[i+1][j][k-1].default_value==1):
                            n+=1
                            
                    if (i!=0 and k!=9):
                        if (mats[i-1][j][k+1].default_value==1):
                            n+=1
                            
                    if (i!=9 and j!=0):
                        if (mats[i+1][j-1][k].default_value==1):
                            n+=1
                            
                    if (i!=0 and j!=9):
                        if (mats[i-1][j+1][k].default_value==1):
                            n+=1
                           
                           
                           
                           
                    if (i!=9 and j!=9 and k!=9):       
                        if (mats[i+1][j+1][k+1].default_value==1):
                            n+=1
                        
                    if (i!=9 and j!=9 and k!=0):  
                        if (mats[i+1][j+1][k-1].default_value==1):
                            n+=1
                            
                    if (i!=9 and j!=0 and k!=9):  
                        if (mats[i+1][j-1][k+1].default_value==1):
                            n+=1
                            
                    if (i!=0 and j!=9 and k!=9):  
                        if (mats[i-1][j+1][k+1].default_value==1):
                            n+=1
                    
                    if (i!=0 and j!=0 and k!=0):  
                        if (mats[i-1][j-1][k-1].default_value==1):
                            n+=1    
                            
                    if (i!=0 and j!=0 and k!=9):  
                        if (mats[i-1][j-1][k+1].default_value==1):
                            n+=1
                            
                    if (i!=0 and j!=9 and k!=0):  
                        if (mats[i-1][j+1][k-1].default_value==1):
                            n+=1
                            
                    if (i!=9 and j!=0 and k!=0):  
                        if (mats[i+1][j-1][k-1].default_value==1):
                            n+=1
                            
                             
                            
                    if (n==5):
                        temp[i][j][k]=1
                    else:
                        temp[i][j][k]=0
                        
                        
    
    bpy.context.scene.frame_set(f)
    for i in range (0,10):
        for j in range (0,10):
            for k in range (0,10):
                if (temp[i][j][k]==0):
                    mats[i][j][k].default_value=0
                elif (temp[i][j][k]==1):
                    mats[i][j][k].default_value=1                      
                mats[i][j][k].keyframe_insert(data_path='default_value',frame=f)
    
'''       
for i in range (0,10):
    for j in range (0,10):
        for k in range (0,10):
            bpy.data.materials['Material.'+str(i)+str(j)+str(k)].node_tree.nodes['Principled BSDF'].inputs[18].default_value=0
             

for i in range (0,10):
    for j in range (0,10):
         for k in range (0,10):
            bpy.ops.mesh.primitive_cube_add(size=1, enter_editmode=False, align='WORLD', location=(i, j, k))
    
'''



    
    