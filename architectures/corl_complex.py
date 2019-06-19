import sys
sys.path.append('../')
from pycore.tikzeng import * 

# defined your arch
arch = [
  to_head( '..' ),
  to_cor(),
  to_begin(),
  # input
  to_input('../examples/snapshot_corl.jpg'),
  to_ConvRelu("conv1", 640, 16, offset="(0,0,0)", to="(0,0,0)", height=32, depth=40, width=4, caption="Conv (9x9) ReLU"),
  to_ConvRelu("conv2", 632, 16, offset="(0,0,0)", to="(3,0,0)", height=30, depth=38, width=4, caption="Conv (5x5) ReLU"),
  to_connection("conv1", "conv2"),
  to_Pool("pool1", offset="(0,0,0)", to="(conv2-east)", height=15, depth=19, width=1),
  to_ConvRelu("conv3", 314, 16, offset="(0,0,0)", to="(7,0,0)", height=14.5, depth=18.5, width=4, caption="Conv (5x5) ReLU"),
  to_connection("pool1", "conv3"),
  to_ConvRelu("conv4", 310, 16, offset="(0,0,0)", to="(10,0,0)", height=13.5, depth=17.5, width=4, caption="Conv (5x5) ReLU"),
  to_connection("conv3", "conv4"),
  to_Pool("pool2", offset="(0,0,0)", to="(conv4-east)", height=6.25, depth=6.25, width=1),
  to_ConvRelu("conv5", 137, 128, offset="(0,0,0)", to="(13,0,0)", height=6, depth=8.5, width=21, caption="Conv (17x17) ReLU"),
  to_connection("pool2", "conv5"),
  to_ConvRelu("conv6", 137, 128, offset="(0,0,0)", to="(19,0,0)", height=6, depth=8.5, width=21, caption="Conv (1x1) ReLU"),
  to_connection("conv5", "conv6"),
  to_ConvSig("conv7", 137, 16, offset="(0,0,0)", to="(25,0,0)", height=6, depth=8.5, width=12, caption="Conv (1x1) Sigmoid"),
  to_connection("conv6", "conv7"),
  to_end()
  ]

def main(): 
  namefile = str(sys.argv[0]).split('.')[0]
  to_generate(arch, namefile + '.tex')

if __name__ == '__main__':
  main()
