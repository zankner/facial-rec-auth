import tensorflow as tf
import tensorflow.contrib as tf_contrib
import numpy as np


##############################################################################
#Layers: Define the layers of your model in this section
##############################################################################
def conv(x, channels, kernel, stride, padding, use_bias, scope):
    with tf.variable_scope(scope):
        x = tf.layers.conv2d(inputs=x, filters=channels,
                kernel_size=kernel, kernel_initializer=weight_init,
                kernel_regularizer=weight_reg,
                strides=stride, use_bias=use_bias, padding=padding)
        return x

def dense(x, units, use_bias, scope):
    with tf.variable_scope(scope):
        x = flatten(x)
        x = tf.layers.dense(x, units=units, kernel_initializer=weight_init,
                kernel_regularizer=weight_reg, use_bias=use_bias)
        return x

#############################################################################
#Sampling: Define the sampling functions of your model in this section
#############################################################################

def flatten(x):
    return tf.layers.flatten(x)

def max_pool(x):
    return tf.layers.average_pooling(x, pool_size=2, strides=2, padding="SAME")

##############################################################################
#Activation: Define the activation functions of your model in this section
##############################################################################

def relu(x):
    return tf.nn.relu(x)

def softmax(x):
    return tf.nn.softmax(x)

##############################################################################
#Normalization: Define the normalization functions of your model in this section
##############################################################################

def batch_norm(x, is_training, scope='batch_norm'):
    return tf_contrib.layers.batch_norm(x,
            decay=0.9, epsilon=1e-05,
            center=True, scale=True, updates_collections=None,
            is_training=is_training, scope=scope)

##############################################################################
#Loss: Define the loss function of your model in this section
##############################################################################

def class_loss(logits,labels):
    loss = tf.losses.softmax_cross_entropy(
            onehot_labels=labels, logits=logits)
    prediction = tf.equal(tf.argmax(logits, -1), tf.argmax(labels, -1))
    accuracy = tf.reduce_mean(tf.cast(prediction, tf.float32))
    return loss, accuracy

################################################################################
#Optimization: Define the optimization function of your model in this section
###############################################################################

def optimizer(lr):
    optimizer = tf.train.AdamOptimizer(learning_rate=lr)
    return optimizer

