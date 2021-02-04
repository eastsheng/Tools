
### 通过pdb文件获得区分自定义原子类型的lammpsdata文件

1. 通过Avogadro优化每个单链：
- 设置力场 Extensions<Molecular Mechanics<Setup Force Field
- 几何优化 Extensions<Optimize Geometry
- 输出pdb格式文件

2. 在MS里修改每个单链中原子力场类型，并同时导出pdb和car文件

3. 把car文件中修改的原子类型 添加到pdb文件中的倒数第二列

4. 通过PACKMOL工具将单链按一定比例混合、添加电极，获得混合的pdb文件

5. 获得的混合pdb文件，在VMD工具中，导出lammpsdata文件

6. 此时，需要文件：
- 混合的pdb文件
- VMD导出的LAMMPS文件
- writelammpsdata_V2.py
- 最后获得区分自定义原子力场类型的lammpsdata文件

7. 手动添加其他参数（键、角、二面角、LJ）

#### 8. 但是 拓扑信息没法给出
具体解决方法见 "Modified_Carfile"