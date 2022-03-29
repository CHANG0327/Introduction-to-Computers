{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "0316.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyO6h8VDanS7axfTtQ95SYMj",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/CHANG0327/Introduction-to-Computers/blob/main/0316.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "id": "lPS9eBHJfyBh"
      },
      "outputs": [],
      "source": [
        "a = 1\n",
        "b = 2\n",
        "c = 3"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(a,b,c)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "bxGyf8K8gMmh",
        "outputId": "deb81311-093e-4034-8933-46c9f5e1dd1f"
      },
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1 2 3\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print([a,b,c])"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "lZTtHq8RgHJF",
        "outputId": "420b9629-b993-49d7-d8c9-8f2b8a90d5e5"
      },
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[1, 2, 3]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(a,[b,c])"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "xIMykPS8iDAA",
        "outputId": "eb24374a-0c46-4520-f745-d442ecfe8d95"
      },
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1 [2, 3]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print('hey','hi','hello')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "DVQtWGg1iJyA",
        "outputId": "a2d286d0-5bff-4eee-f965-2bb092517d3d"
      },
      "execution_count": 6,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "hey hi hello\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print('hey','hi','hello', sep='_')\n",
        "print('hey','hi','hello', sep='\\t')\n",
        "print('hey','hi','hello', sep='\\n')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "eC-pf0vhieJ_",
        "outputId": "5ac229e2-4230-4be1-9c7a-b8ae354e7ccf"
      },
      "execution_count": 7,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "hey_hi_hello\n",
            "hey\thi\thello\n",
            "hey\n",
            "hi\n",
            "hello\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print('早安,')\n",
        "print('同學好!')\n",
        "print('打起精神來!!')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "kQY4kKRcihD6",
        "outputId": "d04b8912-515d-463f-984f-b8ca96e6004f"
      },
      "execution_count": 8,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "早安,\n",
            "同學好!\n",
            "打起精神來!!\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print('早安,','同學好!','打起精神來!!!', sep='\\n')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "QyrSP_o6ijyc",
        "outputId": "5793065a-7fb0-47d8-904f-011840a321e8"
      },
      "execution_count": 9,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "早安,\n",
            "同學好!\n",
            "打起精神來!!!\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(123)\n",
        "print(456)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "KGWmloFkip7j",
        "outputId": "bafb21c4-e3b4-4f92-f8a9-1ab83629a482"
      },
      "execution_count": 10,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "123\n",
            "456\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(123,end=',')\n",
        "print(456)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "j-gNBplgi1I8",
        "outputId": "c800ed20-1cb9-4b91-fc59-bd1146234dd6"
      },
      "execution_count": 11,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "123,456\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print('早安','同學好','打起精神來', sep='_', end = '!!!')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Ox7i2G3di6jf",
        "outputId": "b875ed74-ad19-41d9-c324-6dc934f3d5a5"
      },
      "execution_count": 13,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "早安_同學好_打起精神來!!!"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print('早上好','平安順心','健康如意', sep=',', end ='^^')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "YvNzMecijFwM",
        "outputId": "df487cfa-539e-49c6-9812-f5446ea35f58"
      },
      "execution_count": 14,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "早上好,平安順心,健康如意^^"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "test1 = input('輸入')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "yCNqrHlkjKue",
        "outputId": "9483394f-5c09-4b6d-d233-634009634a14"
      },
      "execution_count": 15,
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "輸入123\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "test1"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "id": "nJPe3Ya8jfN-",
        "outputId": "d836b697-6880-41da-847d-ce39362665db"
      },
      "execution_count": 16,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "'123'"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 16
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "test1+1"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 166
        },
        "id": "V5x7NlwMjnsM",
        "outputId": "2fe64097-1c93-4206-8470-d9340aeec08e"
      },
      "execution_count": 17,
      "outputs": [
        {
          "output_type": "error",
          "ename": "TypeError",
          "evalue": "ignored",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-17-afe2d20a571d>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m()\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0mtest1\u001b[0m\u001b[0;34m+\u001b[0m\u001b[0;36m1\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
            "\u001b[0;31mTypeError\u001b[0m: can only concatenate str (not \"int\") to str"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(type(test1))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "DLNkdbntjpHj",
        "outputId": "30ba890a-ec9b-4c6b-ceb1-953742906a80"
      },
      "execution_count": 18,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "<class 'str'>\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "test2 =int(input('輸入'))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "oWFj_PQljwAU",
        "outputId": "16b57ff2-0883-4777-ccb2-cc5e14c056ea"
      },
      "execution_count": 20,
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "輸入123\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "test2"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "OAzngbvvj48t",
        "outputId": "736ac3d9-0713-43cc-f096-46a43610d8c3"
      },
      "execution_count": 21,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "123"
            ]
          },
          "metadata": {},
          "execution_count": 21
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(type(test2))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "97GY6SAlj_H3",
        "outputId": "8ca69ce6-c1f1-4f71-b6a8-c323ed754538"
      },
      "execution_count": 22,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "<class 'int'>\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "test2+1"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "eh0s2ayzkAby",
        "outputId": "d53f43a2-2369-4d25-bcec-db5a62eb4695"
      },
      "execution_count": 23,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "124"
            ]
          },
          "metadata": {},
          "execution_count": 23
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "test3 = int(input('請輸入月份'))\n",
        "test4 = int(input('請輸入日期'))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "j7W5vHVWkFvd",
        "outputId": "e042c8f0-6434-48cc-ae34-0a1da51a16d8"
      },
      "execution_count": 24,
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "請輸入月份3\n",
            "請輸入日期16\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print('今天是',test3,'月',test4,'號',sep = '')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "f9QNIQe0kLpx",
        "outputId": "2be4840b-1d1c-4211-8a3e-6932ef55c30b"
      },
      "execution_count": 25,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "今天是3月16號\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "test5 = int(input('請輸入國文成績:'))\n",
        "test6 = int(input('請輸入英文成績:'))\n",
        "test7 = int(input('請輸入數學成績:'))\n",
        "print('你的成績總分為:',test5+test6+test7)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "MHy2d6YDkUEj",
        "outputId": "2e62ff28-db3a-4456-a1cb-0681ba65843e"
      },
      "execution_count": 26,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "請輸入國文成績:10\n",
            "請輸入英文成績:20\n",
            "請輸入數學成績:30\n",
            "你的成績總分為: 60\n"
          ]
        }
      ]
    }
  ]
}