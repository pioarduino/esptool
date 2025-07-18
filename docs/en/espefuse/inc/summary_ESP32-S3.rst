.. code-block:: none

    > espefuse -p PORT summary

    Connecting....
    Detecting chip type... ESP32-S3

    === Run "summary" command ===
    EFUSE_NAME (Block) Description  = [Meaningful Value] [Readable/Writeable] (Hex Value)
    ----------------------------------------------------------------------------------------
    Config fuses:
    WR_DIS (BLOCK0)                                    Disable programming of individual eFuses           = 0 R/W (0x00000000)
    RD_DIS (BLOCK0)                                    Disable reading from BlOCK4-10                     = 0 R/W (0b0000000)
    DIS_ICACHE (BLOCK0)                                Set this bit to disable Icache                     = False R/W (0b0)
    DIS_DCACHE (BLOCK0)                                Set this bit to disable Dcache                     = False R/W (0b0)
    DIS_TWAI (BLOCK0)                                  Set this bit to disable CAN function               = False R/W (0b0)
    DIS_APP_CPU (BLOCK0)                               Disable app cpu                                    = False R/W (0b0)
    DIS_DIRECT_BOOT (BLOCK0)                           Disable direct boot mode                           = False R/W (0b0)
    UART_PRINT_CONTROL (BLOCK0)                        Set the default UART boot message output mode      = Enable R/W (0b00)
    PIN_POWER_SELECTION (BLOCK0)                       Set default power supply for GPIO33-GPIO37; set wh = VDD3P3_CPU R/W (0b0)
                                                       en SPI flash is initialized
    BLOCK_USR_DATA (BLOCK3)                            User data
    = 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 R/W
    BLOCK_SYS_DATA2 (BLOCK10)                          System data part 2 (reserved)
    = 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 R/W

    Flash fuses:
    FLASH_TPUW (BLOCK0)                                Configures flash waiting time after power-up; in u = 0 R/W (0x0)
                                                       nit of ms. If the value is less than 15; the waiti
                                                       ng time is the configurable value.  Otherwise; the
                                                        waiting time is twice the configurable value
    FLASH_ECC_MODE (BLOCK0)                            Flash ECC mode in ROM                              = 16to18 byte R/W (0b0)
    FLASH_TYPE (BLOCK0)                                SPI flash type                                     = 4 data lines R/W (0b0)
    FLASH_PAGE_SIZE (BLOCK0)                           Set Flash page size                                = 0 R/W (0b00)
    FLASH_ECC_EN (BLOCK0)                              Set 1 to enable ECC for flash boot                 = False R/W (0b0)
    FORCE_SEND_RESUME (BLOCK0)                         Set this bit to force ROM code to send a resume co = False R/W (0b0)
                                                       mmand during SPI boot

    Identity fuses:
    DISABLE_WAFER_VERSION_MAJOR (BLOCK0)               Disables check of wafer version major              = False R/W (0b0)
    DISABLE_BLK_VERSION_MAJOR (BLOCK0)                 Disables check of blk version major                = False R/W (0b0)
    WAFER_VERSION_MINOR_LO (BLOCK1)                    WAFER_VERSION_MINOR least significant bits         = 0 R/W (0b000)
    PKG_VERSION (BLOCK1)                               Package version                                    = 0 R/W (0b000)
    BLK_VERSION_MINOR (BLOCK1)                         BLK_VERSION_MINOR                                  = 0 R/W (0b000)
    WAFER_VERSION_MINOR_HI (BLOCK1)                    WAFER_VERSION_MINOR most significant bit           = False R/W (0b0)
    WAFER_VERSION_MAJOR (BLOCK1)                       WAFER_VERSION_MAJOR                                = 0 R/W (0b00)
    OPTIONAL_UNIQUE_ID (BLOCK2)                        Optional unique 128-bit ID
    = 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 R/W
    BLK_VERSION_MAJOR (BLOCK2)                         BLK_VERSION_MAJOR of BLOCK2                        = No calib R/W (0b00)
    WAFER_VERSION_MINOR (BLOCK0)                       calc WAFER VERSION MINOR = WAFER_VERSION_MINOR_HI  = 0 R/W (0x0)
                                                       << 3 + WAFER_VERSION_MINOR_LO (read only)

    Jtag fuses:
    SOFT_DIS_JTAG (BLOCK0)                             Set these bits to disable JTAG in the soft way (od = 0 R/W (0b000)
                                                       d number 1 means disable ). JTAG can be enabled in
                                                        HMAC module
    DIS_PAD_JTAG (BLOCK0)                              Set this bit to disable JTAG in the hard way. JTAG = False R/W (0b0)
                                                        is disabled permanently
    STRAP_JTAG_SEL (BLOCK0)                            Set this bit to enable selection between usb_to_jt = False R/W (0b0)
                                                       ag and pad_to_jtag through strapping gpio3 when b
                                                       oth reg_dis_usb_jtag and reg_dis_pad_jtag are equa
                                                       l to 0

    Mac fuses:
    MAC (BLOCK1)                                       MAC address
    = 7c:df:a1:e0:00:58 (OK) R/W
    CUSTOM_MAC (BLOCK3)                                Custom MAC
    = 00:00:00:00:00:00 (OK) R/W

    Security fuses:
    DIS_DOWNLOAD_ICACHE (BLOCK0)                       Set this bit to disable Icache in download mode (b = False R/W (0b0)
                                                       oot_mode[3:0] is 0; 1; 2; 3; 6; 7)
    DIS_DOWNLOAD_DCACHE (BLOCK0)                       Set this bit to disable Dcache in download mode (  = False R/W (0b0)
                                                       boot_mode[3:0] is 0; 1; 2; 3; 6; 7)
    DIS_FORCE_DOWNLOAD (BLOCK0)                        Set this bit to disable the function that forces c = False R/W (0b0)
                                                       hip into download mode
    DIS_DOWNLOAD_MANUAL_ENCRYPT (BLOCK0)               Set this bit to disable flash encryption when in d = False R/W (0b0)
                                                       ownload boot modes
    SPI_BOOT_CRYPT_CNT (BLOCK0)                        Enables flash encryption when 1 or 3 bits are set  = Disable R/W (0b000)
                                                       and disabled otherwise
    SECURE_BOOT_KEY_REVOKE0 (BLOCK0)                   Revoke 1st secure boot key                         = False R/W (0b0)
    SECURE_BOOT_KEY_REVOKE1 (BLOCK0)                   Revoke 2nd secure boot key                         = False R/W (0b0)
    SECURE_BOOT_KEY_REVOKE2 (BLOCK0)                   Revoke 3rd secure boot key                         = False R/W (0b0)
    KEY_PURPOSE_0 (BLOCK0)                             Purpose of Key0                                    = USER R/W (0x0)
    KEY_PURPOSE_1 (BLOCK0)                             Purpose of Key1                                    = USER R/W (0x0)
    KEY_PURPOSE_2 (BLOCK0)                             Purpose of Key2                                    = USER R/W (0x0)
    KEY_PURPOSE_3 (BLOCK0)                             Purpose of Key3                                    = USER R/W (0x0)
    KEY_PURPOSE_4 (BLOCK0)                             Purpose of Key4                                    = USER R/W (0x0)
    KEY_PURPOSE_5 (BLOCK0)                             Purpose of Key5                                    = USER R/W (0x0)
    SECURE_BOOT_EN (BLOCK0)                            Set this bit to enable secure boot                 = False R/W (0b0)
    SECURE_BOOT_AGGRESSIVE_REVOKE (BLOCK0)             Set this bit to enable revoking aggressive secure  = False R/W (0b0)
                                                       boot
    DIS_DOWNLOAD_MODE (BLOCK0)                         Set this bit to disable download mode (boot_mode[3 = False R/W (0b0)
                                                       :0] = 0; 1; 2; 3; 6; 7)
    ENABLE_SECURITY_DOWNLOAD (BLOCK0)                  Set this bit to enable secure UART download mode   = False R/W (0b0)
    SECURE_VERSION (BLOCK0)                            Secure version (used by ESP-IDF anti-rollback feat = 0 R/W (0x0000)
                                                       ure)
    BLOCK_KEY0 (BLOCK4)
    Purpose: USER
                Key0 or user data
    = 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 R/W
    BLOCK_KEY1 (BLOCK5)
    Purpose: USER
                Key1 or user data
    = 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 R/W
    BLOCK_KEY2 (BLOCK6)
    Purpose: USER
                Key2 or user data
    = 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 R/W
    BLOCK_KEY3 (BLOCK7)
    Purpose: USER
                Key3 or user data
    = 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 R/W
    BLOCK_KEY4 (BLOCK8)
    Purpose: USER
                Key4 or user data
    = 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 R/W
    BLOCK_KEY5 (BLOCK9)
    Purpose: USER
                Key5 or user data
    = 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 R/W

    Spi Pad fuses:
    SPI_PAD_CONFIG_CLK (BLOCK1)                        SPI_PAD_configure CLK                              = 0 R/W (0b000000)
    SPI_PAD_CONFIG_Q (BLOCK1)                          SPI_PAD_configure Q(D1)                            = 0 R/W (0b000000)
    SPI_PAD_CONFIG_D (BLOCK1)                          SPI_PAD_configure D(D0)                            = 0 R/W (0b000000)
    SPI_PAD_CONFIG_CS (BLOCK1)                         SPI_PAD_configure CS                               = 0 R/W (0b000000)
    SPI_PAD_CONFIG_HD (BLOCK1)                         SPI_PAD_configure HD(D3)                           = 0 R/W (0b000000)
    SPI_PAD_CONFIG_WP (BLOCK1)                         SPI_PAD_configure WP(D2)                           = 0 R/W (0b000000)
    SPI_PAD_CONFIG_DQS (BLOCK1)                        SPI_PAD_configure DQS                              = 0 R/W (0b000000)
    SPI_PAD_CONFIG_D4 (BLOCK1)                         SPI_PAD_configure D4                               = 0 R/W (0b000000)
    SPI_PAD_CONFIG_D5 (BLOCK1)                         SPI_PAD_configure D5                               = 0 R/W (0b000000)
    SPI_PAD_CONFIG_D6 (BLOCK1)                         SPI_PAD_configure D6                               = 0 R/W (0b000000)
    SPI_PAD_CONFIG_D7 (BLOCK1)                         SPI_PAD_configure D7                               = 0 R/W (0b000000)

    Usb fuses:
    DIS_USB_OTG (BLOCK0)                               Set this bit to disable USB function               = False R/W (0b0)
    USB_EXCHG_PINS (BLOCK0)                            Set this bit to exchange USB D+ and D- pins        = False R/W (0b0)
    USB_EXT_PHY_ENABLE (BLOCK0)                        Set this bit to enable external PHY                = False R/W (0b0)
    DIS_USB_JTAG (BLOCK0)                              Set this bit to disable function of usb switch to  = False R/W (0b0)
                                                       jtag in module of usb device
    DIS_USB_SERIAL_JTAG (BLOCK0)                       Set this bit to disable usb device                 = False R/W (0b0)
    USB_PHY_SEL (BLOCK0)                               This bit is used to switch internal PHY and extern
    = internal PHY is assigned to USB Device while external PHY is assigned to USB OTG R/W (0b0)
                                                       al PHY for USB OTG and USB Device
    DIS_USB_SERIAL_JTAG_ROM_PRINT (BLOCK0)             USB printing                                       = Enable R/W (0b0)
    DIS_USB_SERIAL_JTAG_DOWNLOAD_MODE (BLOCK0)         Set this bit to disable UART download mode through = False R/W (0b0)
                                                        USB
    DIS_USB_OTG_DOWNLOAD_MODE (BLOCK0)                 Set this bit to disable download through USB-OTG   = False R/W (0b0)

    Vdd fuses:
    VDD_SPI_XPD (BLOCK0)                               SPI regulator power up signal                      = False R/W (0b0)
    VDD_SPI_TIEH (BLOCK0)                              If VDD_SPI_FORCE is 1; determines VDD_SPI voltage
    = VDD_SPI connects to 1.8 V LDO R/W (0b0)
    VDD_SPI_FORCE (BLOCK0)                             Set this bit and force to use the configuration of = False R/W (0b0)
                                                        eFuse to configure VDD_SPI

    Wdt fuses:
    WDT_DELAY_SEL (BLOCK0)                             RTC watchdog timeout threshold; in unit of slow cl = 40000 R/W (0b00)
                                                       ock cycle

    Flash voltage (VDD_SPI) determined by GPIO45 on reset (GPIO45=High: VDD_SPI pin is powered from internal 1.8V LDO
    GPIO45=Low or NC: VDD_SPI pin is powered directly from VDD3P3_RTC_IO via resistor Rspi. Typically this voltage is 3.3 V).
