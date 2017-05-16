import tensorflow as tf
#
import seaborn as sn
import pandas as pd
import matplotlib.pyplot as plt
#
import numpy as np
#
import time

import dataset
import neural

test_success = 0
start = time.time()
# test training and result 5 times
for x in range(0, 5):

    [w1, w2, b1, b2, epoch, err, sess] = neural.train()

    print('epoch:', epoch, 'mse:', err)

    if err < 0.01: #target
        test_success = test_success + 1

    # test results
    """output_array = np.zeros((2, 2), dtype=np.float32)
    t_train_in = [
        [1., 1.],
        [1., 0.],
        [0., 1.],
        [0., 0.],
    ]"""
    t_out1 = tf.sigmoid(tf.add(tf.matmul(dataset.train_in, w1), b1))
    t_out2 = tf.sigmoid(tf.add(tf.matmul(t_out1, w2), b2))
    t_result = sess.run([t_out2])

    print('result', t_result)

    """for y in range(0, 5):
        t_out1 = tf.tanh(tf.add(tf.matmul(t_train_in, w1), b1))
        t_out2 = tf.tanh(tf.add(tf.matmul(t_out1, w2), b2))
        t_result = sess.run([t_out2])

        # add to graph
        if t_result[0][0] < 0.5:
            print("v")
            output_array[0][0] = output_array[0][0] + 1
        else:
            output_array[0][1] = output_array[0][1] + 1

        if t_result[0][3] < 0.5:
            output_array[0][0] = output_array[0][0] + 1
        else:
            output_array[0][1] = output_array[0][1] + 1

        ##
        if t_result[0][1] > 0.5:
            output_array[1][1] = output_array[1][1] + 1
        else:
            output_array[1][0] = output_array[1][0] + 1

        if t_result[0][2] > 0.5:
            output_array[1][1] = output_array[1][1] + 1
        else:
            output_array[1][0] = output_array[1][0] + 1"""


        # output_array = output_array + t_result[0]
        # print('res', t_result[0][0])
        # print('res', t_result)
        # print('res2', t_result[0] + t_result[0])

    #confusion_matrix_graphic(output_array)

    """confusion_matrix_graphic(
            [[33,2,0,0,0,0,0,0,0,1,3],
            [3,31,0,0,0,0,0,0,0,0,0],
            [0,4,41,0,0,0,0,0,0,0,1],
            [0,1,0,30,0,6,0,0,0,0,1],
            [0,0,0,0,38,10,0,0,0,0,0],
            [0,0,0,3,1,39,0,0,0,0,4],
            [0,2,2,0,4,1,31,0,0,0,2],
            [0,1,0,0,0,0,0,36,0,2,0],
            [0,0,0,0,0,0,1,5,37,5,1],
            [3,0,0,0,0,0,0,0,0,39,0],
            [0,0,0,0,0,0,0,0,0,0,38]])"""

    # variables_names =[v.name for v in tf.trainable_variables()]
    # values = sess.run(variables_names)
    # for k,v in zip(variables_names, values):
    #     print(k, v)


print('time', time.time() - start)
print('success ', test_success)
