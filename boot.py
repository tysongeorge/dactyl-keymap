import board
from kmk.bootcfg import bootcfg
# import storage

# handling drive renaming on plugin
# storage.remount("/", readonly=False)
# m = storage.getmount("/")
# m.label = "DACTYL"
# storage.remount("/", readonly=True)
# 
# storage.enable_usb_drive()

# other boot options for the keyboard
bootcfg(
    sense   = board.GP4, # col
    source  = board.A0,  # row 
    nkro    = True,
    storage = True,
    usb_id  = ("KMK", "DactyL"),
)
