from inc_noesis import *

def registerNoesisTypes():
    handle = noesis.register("PS2Nemo", ".ghg")
    noesis.setHandlerTypeCheck(handle, CheckType)
    noesis.setHandlerLoadModel(handle, LoadModel)
    #noesis.logPopup()
    return 1



def CheckType(data):
    return 1

def LoadModel(data, mdlList):

    global bone_parent

    f = NoeBitStream(data)
    vertices=[]
    vertices2=[]
    meshes = []
    bones = []
    #faces=[0,0,0]
    PosMatrix = [0]
    PosBones = []
    #wrong
    fa = -1
    fb = 0
    fc = 1
    parent_id=-1
    #
    FileSize_ = f.readInt()
    unk1 = f.readInt()
    TextureCount = f.readInt()
    TextureEntrySize1 = f.readInt()
    MaterialCount = f.readInt()
    MaterialEntrySize1 = f.readInt()
    BoneCount = f.readInt()
        
    BoneEntrySize1 = f.readInt()
    BoneEntrySize2 = f.readInt()
    BoneEntrySize3 = f.readInt()
    f.seek(BoneEntrySize1-40,1)
    for k in range(BoneCount):
        
        boneMat_ = NoeMat44.fromBytes(f.read(64),0).toMat43().inverse() # unk
        bdiv4_v00 = f.readFloat()
        bdiv4_v04 = f.readFloat()
        bdiv4_v08 = f.readFloat()
        f.seek(4,1)
        bone_parent = f.readByte()
        name_offset = f.readInt()-1
        f.seek(11,1)
        
    for x in range(BoneCount):
        boneMat = NoeMat44.fromBytes(f.read(64),0).toMat43().inverse() # pos
        #bones.append(NoeBone(k+x,"dragonjan_bones",boneMat,None,bone_parent))

    for j in range(BoneCount):
        boneMa = NoeMat44.fromBytes(f.read(64),0).toMat43().inverse() # negative pos
        bones.append(NoeBone(k+x+j, "dragonjan_bones",boneMa,None,bone_parent))
    
        
    

    f.seek(0)
    FileSize = f.readInt()
    f.seek(-4,1)
    for i in range(int(FileSize)):

        Chunk = f.readInt()
        if Chunk == int(16777475):
            f.seek(2,1)
            VertexCount = f.readByte()
            f.seek(1,1)
            for i in range(VertexCount):
                vx = f.readFloat()
                vy = f.readFloat()
                vz = f.readFloat()
                nz = f.readFloat()
                vertices.append(NoeVec3([vx,vy,vz]))
        elif Chunk == int(16777731):
            f.seek(2,1)
            VertexCount = f.readByte() // 2
            f.seek(1,1)
            for i in range(VertexCount):
                vx = f.readShort() / 4096.0
                vy = f.readShort() / 4096.0
                vz = f.readShort() / 4096.0
                nz = f.readShort() / 4096.0
                f.seek(8,1)
                vertices.append(NoeVec3([vx,vy,vz]))
            
        elif Chunk == int(16777732):
            f.seek(2,1)
            VertexCount = f.readByte() // 2
            f.seek(1,1)
            for i in range(VertexCount):
                vx = f.readFloat()
                vy = f.readFloat()
                vz = f.readFloat()
                nz = f.readFloat()
                f.seek(16,1)
                vertices.append(NoeVec3([vx,vy,vz]))
            
    mesh = NoeMesh([], vertices, "default")
    meshes.append(mesh)
    mdl = NoeModel(meshes)
    mdl.setBones(bones)
    mdlList.append(mdl)
    return 1
                
            

