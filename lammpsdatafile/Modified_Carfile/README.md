
### 通过pdb文件获得区分自定义原子类型的lammpsdata文件

1. 通过Avogadro优化每个单链：
- 设置力场 Extensions<Molecular Mechanics<Setup Force Field
- 几何优化 Extensions<Optimize Geometry
- 输出pdb格式文件

2. 在MS里修改每个单链中原子力场类型，并同时导出pdb和car文件

3. 把car文件中修改的原子类型 添加到pdb文件中的倒数第二列

4. 通过PACKMOL工具将单链按一定比例混合、添加电极，获得混合的pdb文件

5. 获得的混合pdb文件，在MS中，导出car文件

6. 此时，需要文件：
- 混合的pdb文件
- MS导出的car、mdf文件
- 运行rewrite_MS_car.py
- 最后获得区分自定义原子力场类型的car、mdf文件

7. 最终，通过Lammps Tool "msi2lmp.exe" 导出含有拓扑信息的data
8. 最后自己修改其他需要的参数。