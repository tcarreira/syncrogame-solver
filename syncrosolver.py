#!/usr/bin/env python3¡
import Syncro


def main():
    game = Syncro.Level_0()
    game.solve()
    game = Syncro.Level_1()
    game.solve()
    game = Syncro.Level_2()
    game.solve()


if __name__ == '__main__':
    main()
