# clash-yangon 说明

## 安装

直接使用 pacman 安装 gapoon源（https://ghs.gapoon.me/~gapoon）中的 clash-yangon 包

## 使用

clash-yangon 是为了关机时记住 clash 中的节点而写的脚本。其包含有 system/clash-yangon@.service 和 user/clash-yangon.service 两个 systemd unit，一个名为 clash-yangon 的脚本和其他若干脚本。

在使用时，直接开启对应的服务即可。如：

```shell
systemctl enable clash-yangon.service --user --now
# 启用该服务，会以当前用户身份运行 clash 并将当前 clash 选择的节点保存到当前用户家目录中。
```

或者

```shell
systemctl enable clash-yangon@用户名.service --now
# 启用该服务，会以 root 身份运行 clash，并将当前 clash 选择的节点保存到当前用户家目录中
```

两者仅需启用一个即可。

## 配置 clash 参数

可以在 /etc/clash-yangon.conf 文件中配置 clash 的启动参数，具体格式参见该文件注释内容

## 其他说明

===当前还未支持，在 experiment 分支===

/usr/bin/clash-yangon 会从当前执行用户（或者执行 sudo 的用户）的家目录读取保存的节点选择，并启动 clash。具体用法如下：

```shell
clash-yangon [用户名] -- [传给 clash 的参数]
	用户名				用户名置顶后，会从指定用户的家目录读取存储的节点选择
	传给clash的参数	   填写要传给 clash 的参数
 两参数均非必须
```

使用示例：

```shell
clash-yangon
clash-yangon yangon
clash-yangon yangon -- -t

```
