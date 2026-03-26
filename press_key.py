import sys

def get_pressed_key():
    if sys.platform == 'win32':
        # ========== Windows 系统 ==========
        import msvcrt
        if msvcrt.kbhit():
            # 读取第一个字节
            key = msvcrt.getch()
            # 处理方向键（双字节）
            if key in (b'\xe0', b'\x00'):
                key = msvcrt.getch()
                key_map = {b'H': 'UP', b'P': 'DOWN', b'K': 'LEFT', b'M': 'RIGHT'}
                return key_map.get(key, f"")
            # 处理普通键/基础特殊键
            key_str = key.decode('gbk', errors='ignore')  # Windows 用 gbk 编码更兼容
            if key_str == '\r':
                return 'ENTER'
            elif key_str == '\x1b':
                return 'ESC'
            else:
                return key_str
        return None
    else:
        # ========== Linux/macOS 系统 ==========
        import tty
        import termios
        import select
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            # 非阻塞检测是否有输入
            if select.select([sys.stdin], [], [], 0) != ([sys.stdin], [], []):
                # 读取第一个字符
                key = sys.stdin.read(1)
                # 方向键的第一个字符是 ESC（\x1b），后续还有 2 个字节
                if ord(key) == 27:
                    # 继续读取剩下的字节（[ 和 A/B 组合）
                    key2 = sys.stdin.read(1)
                    key3 = sys.stdin.read(1)
                    if key2 == '[':
                        if key3 == 'A':
                            return 'UP'    # 上键
                        elif key3 == 'B':
                            return 'DOWN'  # 下键
                        else:
                            return f"其他方向键({key3})"
                    else:
                        return 'ESC'
                # 普通键/基础特殊键
                elif ord(key) == 13:
                    return 'ENTER'
                else:
                    return key
            return None
        finally:
            # 必须恢复终端设置，避免异常
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)