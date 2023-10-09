import storage, board
from kmk.bootcfg import bootcfg

# handling drive renaming on plugin
storage.remount("/", readonly=False)
m = storage.getmount("/")
m.label = "DACTYL"
storage.remount("/", readonly=True)

storage.enable_usb_drive()

## other boot options for the keyboard
# bootcfg(
    # sense  = board.GP2, # col
    # source = board.A2, # row
    # midi   = False,
    # mouse  = False,
    # nkro   = True,
    # usb_id = ("KMK", "Dactyl")
# )
