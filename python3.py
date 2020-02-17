{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "python3.py",
      "provenance": [],
      "collapsed_sections": [],
      "authorship_tag": "ABX9TyMvVX4NMatDO2hawPolmMM7"
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "metadata": {
        "id": "2S5C-IFufDqB",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 68
        },
        "outputId": "b0a7e6ee-9162-483f-e19a-fe88401623a1"
      },
      "source": [
        "def sum(i1,i2) :\n",
        "  result = 1\n",
        "  for i in range(i1,i2+1) :\n",
        "    result=result+i\n",
        "  return result\n",
        "        \n",
        "\n",
        "\n",
        "def main() :\n",
        "  print(\"Sum From 1 to 10:\",sum(1,10))\n",
        "  print(\"Sum From 20 to 27 :\",sum(20,27))\n",
        "\n",
        "main()\n",
        "\n",
        "  "
      ],
      "execution_count": 17,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Sum From 1 to 10: 56\n",
            "Sum From 20 to 27 : 189\n",
            "Greatest comman Divisor: 1\n"
          ],
          "name": "stdout"
        }
      ]
    }
  ]
}