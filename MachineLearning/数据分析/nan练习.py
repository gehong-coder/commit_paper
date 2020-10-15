import numpy as np

#建立
#数据的清理，将数据中间出现nan的地方进行替换
'''对每一列进行遍历，判断，看看是不是nan，如果是的话，进行替换'''

def fill_ndary(t1):
    for i in range(t1.shape[1]):#遍历每一列，对每一列会有一个值，这个值代表了这个这个形状的大小
        tem_col=t1[:,i]#
        #判断是否存在nan
        nan_num = np.count_nonzero(tem_col!=tem_col)
        if nan_num!=0:
            tem_col_not_nan=tem_col[tem_col==tem_col]#值不为nan的所有值
            tem_col[np.isnan(tem_col)]=tem_col_not_nan.mean()#将所有的值进行赋值
    return t1

if __name__ == '__main__':
    t1 = np.arange(12).reshape(3, 4).astype("float")
    t1[1, 2:] = np.nan  # 中间的nan已经被替换列
    print(t1)
    t1=fill_ndary(t1)#已经进行了替换，将均值进行替换，
    print(t1)