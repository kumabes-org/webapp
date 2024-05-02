package br.com.kumabe.webapp.controllers;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.servlet.ModelAndView;

import java.net.InetAddress;
import java.net.UnknownHostException;

@Controller
public class WebappController {

    @Value("${app.version:unknown}")
    private String applicationVersion;

    @GetMapping
    public ModelAndView index() throws UnknownHostException {
        ModelAndView modelAndView = new ModelAndView("index");
        // Local address
        String hostAddress = InetAddress.getLocalHost().getHostAddress();
        String hostName = InetAddress.getLocalHost().getHostName();
        modelAndView.addObject("applicationVersion", applicationVersion);
        modelAndView.addObject("hostAddress", hostAddress);
        modelAndView.addObject("hostName", hostName);
        return modelAndView;
    }
}
