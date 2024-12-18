from PyPDF2 import PdfMerger

merger = PdfMerger()

# 打开两个输入文件
input1 = open('doc1.pdf', 'rb')
input2 = open('doc2.pdf', 'rb')

# 将第一个文件添加到合并器中
merger.append(input1)

# 将第二个文件添加到合并器中，从第2页开始
merger.merge(position=2, fileobj=input2, pages=(0, 1))

# 打开输出文件
output = open('doc-output.pdf', 'wb')

# 将合并后的 PDF 写入输出文件
merger.write(output)

# 关闭文件
input1.close()
input2.close()
output.close()