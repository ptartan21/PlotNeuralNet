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
  to_Conv("conv1", 96, 16, offset="(0,0,0)", to="(0,0,0)", height=24, depth=24, width=4),
  to_Conv("conv2", 88, 16, offset="(0,0,0)", to="(2,0,0)", height=22, depth=22, width=4, caption="Conv 9x9"),
  to_connection("conv1", "conv2"),
  to_Conv("conv3", 84, 16, offset="(0,0,0)", to="(4,0,0)", height=21, depth=21, width=4, caption="Conv 5x5"),
  to_connection("conv2", "conv3"),
  to_Pool("pool1", offset="(0,0,0)", to="(conv3-east)", height=10.5, depth=10.5, width=1),
  to_Conv("conv4", 38, 16, offset="(0,0,0)", to="(6.5,0,0)", height=9.5, depth=9.5, width=4, caption="Conv 5x5"),
  to_connection("pool1", "conv4"),
  to_Conv("conv5", 34, 16, offset="(0,0,0)", to="(8.5,0,0)", height=8.5, depth=8.5, width=4, caption="Conv 5x5"),
  to_connection("conv4", "conv5"),
  to_Pool("pool2", offset="(0,0,0)", to="(conv5-east)", height=4.5, depth=4.5, width=1),
  to_Conv("conv6", 1, 128, offset="(0,0,0)", to="(11.5,0,0)", height=1, depth=1, width=21, caption="Conv 17x17"),
  to_connection("pool2", "conv6"),
  to_Conv("conv7", 1, 128, offset="(0,0,0)", to="(17,0,0)", height=1, depth=1, width=21, caption="Conv 1x1"),
  to_connection("conv6", "conv7"),
  to_Conv("conv8", 1, 16, offset="(0,0,0)", to="(22.5,0,0)", height=1, depth=1, width=12, caption="Conv 16x16"),
  to_connection("conv7", "conv8"),
  to_end()
  ]

def main(): 
  namefile = str(sys.argv[0]).split('.')[0]
  to_generate(arch, namefile + '.tex')

if __name__ == '__main__':
  main()
