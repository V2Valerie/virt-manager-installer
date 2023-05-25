import os

def for_systemd():
	print("Installing components... \n")
	os.system("sudo pacman -Syy qemu-full virt-manager libvirt dnsmasq")

	print("adding the current user to the libvirt group... \n")
	os.system("sudo usermod -a -G libvirt $USER")

	print("starting and enabling libvirt... \n")
	os.system("sudo systemctl start libvirtd")
	os.system("sudo systemctl enable libvirtd")

	print("starting the default virtual network in the Virsh hypervisor management tool... \n")
	os.system("sudo virsh net-start default")
	os.system("sudo virsh net-autostart default")

	print("Success, you can now open virt-manager \n")


def for_openrc():
	print("Installing components... \n")
	os.system("sudo pacman -Syy qemu-full virt-manager libvirt libvirt-openrc dnsmasq")

	print("Adding the current user to the libvirt group... \n")
	os.system("sudo usermod -a -G libvirt $USER")

	print("Starting and enabling libvirt... \n")
	os.system("sudo rc-service libvirtd start")
	os.system("sudo r-update add libvirtd default")

	print("Starting the default virtual network in the Virsh hypervisor management tool... \n")
	os.system("sudo virsh net-start default")
	os.system("sudo virsh net-autostart default")

	print("Success, you can now open virt-manager \n")


# Main
print("[1] Systemd\n[2] OpenRC\n")
option = int(input("[?] Select init system 1/2 : ").strip())
if option == 1:
	for_systemd()
elif option == 2:
	for_openrc()
else:
	print("invalid option")