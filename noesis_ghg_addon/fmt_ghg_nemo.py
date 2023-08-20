from inc_noesis import *
import os

#export options
TextureCount_ON = False
MaterialCount_ON = False
BoneCount_ON = False
NamedTable_ON = False
UV_ON = False
VertexColors_ON = False
PointClouds_ON = False
Weights_ON = False

def registerNoesisTypes():
    handle = noesis.register("PS2Nemo", ".ghg")
    noesis.setHandlerTypeCheck(handle, CheckType)
    noesis.setHandlerLoadModel(handle, LoadModel)
    noesis.setHandlerWriteModel(handle, WriteModel)
    #noesis.logPopup()
    return 1



def CheckType(data):
    return 1

def LoadModel(data, mdlList):

    f = NoeBitStream(data)
    vertices=[]
    vertices2=[]
    meshes = []
    bones = []
    faces = [0,0,0]
    PosMatrix = [0]
    PosBones = []
    bone_pare = []
    names = None
    #wrong
    fa = -3
    fb = -2
    fc = -1
    parent_id=-1
    #
    FileSize_ = f.readInt()
    unk1 = f.readInt()
    TextureCount = f.readInt()
    TextureEntrySize1 = f.readInt()
    MaterialCount = f.readInt()
    MaterialEntrySize1 = f.readInt()
    BoneCount = f.readInt()
    f.seek(-4,1)
    BoneCount2 = f.readInt()
    f.seek(-4,1)
    BoneCount3 = f.readInt()
        
    BoneEntrySize1 = f.readInt()
    BoneEntrySize2 = f.readInt()
    BoneEntrySize3 = f.readInt()
    unk2 = f.readInt()
    unkEntrySize1 = f.readInt()
    namedtableStartEntry1 = f.readInt()
    namedtableEntrySize1 = f.readInt()
    f.seek(namedtableStartEntry1-56,1)
    names = f.read(namedtableEntrySize1)
    f.seek(0)
    f.seek(40,1)
    f.seek(BoneEntrySize1-40,1)
    bone_id = -1
    for k in range(BoneCount):
        boneMat = NoeMat44.fromBytes(f.read(64),0).toMat43().inverse()
        f.seek(4,1)
        f.seek(4,1)
        f.seek(4,1)
        f.seek(4,1)
        bone_parent = f.readByte()
        name_offset = f.readInt()-1
        f.seek(11,1)
    for i in range(BoneCount):
        boneMat = NoeMat44.fromBytes(f.read(64),0).toMat43().inverse() # negative pos
    for j in range(BoneCount):
        boneMa = NoeMat44.fromBytes(f.read(64),0).toMat43().inverse() # correct pos
        bones.append(NoeBone(k+i+j, "dragonjan_bones",boneMa,None,bone_parent))

    f.seek(0)
    WeightFileSize = f.readInt()
    f.seek(-4,1)
    for i in range(int(WeightFileSize)):
        pass
    
    
        
    

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
            
    mesh = NoeMesh(faces, vertices, "default")
    meshes.append(mesh)
    mdl = NoeModel(meshes)
    mdl.setBones(bones)
    mesh.setWeights([])
    mdlList.append(mdl)
    print(faces)
    return 1

def WriteModel(mdl, f):
    pass
        
    
                
            

