<div class="page">

# MACSEC for point ti point

\

# MACSEC POINT TO POINT

\#We create keys

<div class="codebox">

    dd if=/dev/urandom count=16 bs=1 2>/dev/null | hexdump -e '1/2 "%04x"'
    dd if=/dev/urandom count=32 bs=1 2>/dev/null | hexdump -e '1/2 "%04x"'

</div>

In UBUNTU SERVER you have to install NMCLI:

<div class="codebox">

    sudo apt install network-manager

</div>

Modify the NETPLAN to include the first two lines, version and
renderer:

<div class="codebox">

    network:
      version: 2
      renderer: NetworkManager
      ethernets:

</div>

We check the configuration:

<div class="codebox">

    sudo nano /etc/NetworkManager/NetworkManager.conf

</div>

It must appear at least:

<div class="codebox">

    [main]
        plugins=keyfile

</div>

And we restart the NetworkManager:

<div class="codebox">

    sudo systemctl restart NetworkManager

</div>

Macsec must be included as an unmanaged device

<div class="codebox">

    sudo nano /usr/lib/NetworkManager/conf.d/10-globally-managed-devices.conf

</div>

We add.

<div class="codebox">

    [keyfile]
        unmanaged-devices=*,except:type:wifi,except:type:ethernet

</div>

And we recharge:

<div class="codebox">

    sudo systemctl reload NetworkManager

</div>


## on nmcli
<div class="codebox">

    nmcli connection add type macsec con-name macsec0 ifname macsec0
    connection.autoconnect yes macsec.parent enp0s8 macsec.mode psk
    macsec.mka-cak 50b71a8ef0bd5751ea76de6d6c98c03a macsec.mka-ckn
    f2b4297d39da7330910a74abc0449feb45b5c0b9fc23df1430e1898fcf1c4550

    nmcli connection modify macsec0 ipv4.method manual ipv4.addresses
    '192.0.2.1/24' ipv4.gateway '192.0.2.254' ipv4.dns '192.0.2.253'
</div>

Verify that the traffic is encrypted:
<div class="codebox">

    `# tcpdump -nn -i enp1s0`
</div>
Optional: Display the unencrypted traffic:
<div class="codebox">

    `# tcpdump -nn -i macsec0`
</div>
Display MACsec statistics:
<div class="codebox">

    `# ip macsec show`
</div>
Display individual counters for each type of protection:
<div class="codebox">
    integrity-only (encrypt off) and encryption (encrypt on)

    `# ip -s macsec show`
</div>