# -*- coding:utf8 -*-

import os

#全局配置段
GLOBAL={

    "Host": os.getenv("swarmops_host", "0.0.0.0"),
    #Application run network address, you can set it `0.0.0.0`, `127.0.0.1`, ``;

    "Port": int(os.getenv("swarmops_port", 10130)),
    #Application run port, default port;

    "Debug": os.getenv("swarmops_debug", True),
    #The development environment is open, the production environment is closed, which is also the default configuration.

    "LogLevel": os.getenv("swarmops_loglevel", "DEBUG"),
    #应用程序写日志级别，目前有DEBUG，INFO，WARNING，ERROR，CRITICAL

    "SwarmStorageMode": os.getenv("swarmops_swarmstoragemode", "redis"),
    #存储Swarm集群信息的方式

    "Interest.blog.Url": os.getenv("swarmops_interest_blog_url", "https://www.saintic.com/home/")

}

#生产环境配置段
PRODUCT={

    "ProcessName": "SwarmOps",
    #Custom process, you can see it with "ps aux|grep ProcessName".

    "ProductType": os.getenv("swarmops_producttype", "tornado"),
    #生产环境启动方法，可选`gevent`, `tornado`。
}

#STORAGE配置段
STORAGE={
    "Connection": os.getenv("swarmops_StorageConnection", "redis://ip:port:password"),

    "SwarmKey": os.getenv("swarmops_StorageSwarmKey", "Swarm_All"),

    "ActiveKey": os.getenv("swarmops_StorageActiveKey", "Swarm_Active"),
}

SSO={

    "SSO.URL": os.getenv("swarmops_ssourl", "https://passport.saintic.com"),
    #The passport(SSO Authentication System) Web Site URL.

    "SSO.PROJECT": PRODUCT["ProcessName"],
    #SSO request application.
}
