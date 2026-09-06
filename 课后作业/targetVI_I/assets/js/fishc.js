
var touchclick = ('ontouchstart' in document) ? 'touchstart' : 'click';
var device = (navigator.userAgent.indexOf('iPhone') > 0 || navigator.userAgent.indexOf('iPad') > 0 || navigator.userAgent.indexOf('iPod') > 0 || navigator.userAgent.indexOf('Android') > 0) ? 'sp' : 'pc';
var scrollTop = document.scrollingElement || document.documentElement;
var responsive = '';

$(function(){
	createjs.Ticker.framerate = 60;
	var manifest = [];
	$('img').each(function(){ manifest.push($(this).attr('src')); });
  if($('main').hasClass('top')){
  	manifest.push('./assets/img/avex.png');
  	manifest.push('./assets/img/page.png');
  	manifest.push('./assets/img/arrow_top.png');
  	manifest.push('./assets/img/arrow_left.png');
  	manifest.push('./assets/img/swiper_prev.png');
  	manifest.push('./assets/img/swiper_next.png');
  	manifest.push('./assets/img/arrow_blank.png');
  	manifest.push('./assets/img/movie_play.png');
  	manifest.push('./assets/img/profile_pc.png');
  	manifest.push('./assets/img/profile_sp.png');
  	manifest.push('./assets/img/music_play.png');
  	manifest.push('./assets/img/music_pause.png');
  }else{
  	manifest.push('../assets/img/avex.png');
  	manifest.push('../assets/img/page.png');
  	manifest.push('../assets/img/arrow_top.png');
  	manifest.push('../assets/img/arrow_left.png');
  	manifest.push('../assets/img/swiper_prev.png');
  	manifest.push('../assets/img/swiper_next.png');
  	manifest.push('../assets/img/arrow_blank.png');
  	manifest.push('../assets/img/movie_play.png');
  	manifest.push('../assets/img/profile_pc.png');
  	manifest.push('../assets/img/profile_sp.png');
  	manifest.push('../assets/img/music_play.png');
  	manifest.push('../assets/img/music_pause.png');
  }
	var loadQueue = new createjs.LoadQueue();
	loadQueue.on('complete', function(e){

  	$(window).on('resize', function() { responsive = (768 < window.innerWidth) ? 'pc' : 'sp' }).trigger('resize');

    if($('main').hasClass('top')){
    	$(window).on('resize', function() { $('header.page').height(window.innerHeight); }).trigger('resize');
      var slider_swiper = new Swiper('section.slider div.section div.slider div.swiper-container', {
    		speed:500,
    		effect:'slide',
    		slidesPerView:'auto',
    		centeredSlides:true,
    		navigation:{ prevEl:'section.slider div.section div.slider div.swiper-container div.swiper-button-prev', nextEl:'section.slider div.section div.slider div.swiper-container div.swiper-button-next' },
    		pagination:{ el:'section.slider div.section div.slider div.swiper-container div.swiper-pagination', type:'bullets', clickable:true },
      });
      var movie_swiper = new Swiper('section.movie div.section div.movie div.swiper-container', {
    		speed:500,
    		effect:'slide',
    		slidesPerView:'auto',
    		centeredSlides:true,
    		navigation:{ prevEl:'section.movie div.section div.movie div.swiper-container div.swiper-button-prev', nextEl:'section.movie div.section div.movie div.swiper-container div.swiper-button-next' },
    		pagination:{ el:'section.movie div.section div.movie div.swiper-container div.swiper-pagination', type:'bullets', clickable:true },
      });
			$(window).on('scroll', function(){
				if($(window).scrollTop() <= 0) $('body').removeClass('top');
				else $('body').addClass('top');
			}).trigger('scroll');
			var mousewheelevent = 'onwheel' in document ? 'wheel' : 'onmousewheel' in document ? 'mousewheel' : 'DOMMouseScroll';
			$(document).on(mousewheelevent,function(e){
				var delta = e.originalEvent.deltaY ? -(e.originalEvent.deltaY) : e.originalEvent.wheelDelta ? e.originalEvent.wheelDelta : -(e.originalEvent.detail);
				if (delta < 0){
					if(!$('body').hasClass('top')){
						$('html, body').stop().animate({ scrollTop:$('nav.page').offset().top }, { duration:500, easing:'easeOutCubic' });
					}
				}
			});

  		(function changeTwitter(){
  			if ($('section.twitter iframe.twitter-timeline').contents().find('body').length > 0) {
  				setTimeout(function(){
  					$('section.twitter div.twitter').html($('section.twitter iframe.twitter-timeline').contents().find('body').html());
  					$('section.twitter div.twitter .timeline-Viewport').css({ 'height':'auto' });
  					$('section.twitter div.twitter a[href^=http]').not('[href*="'+location.hostname+'"]').attr({target:'_blank'});
  					if(responsive == 'pc') $('section.twitter div.twitter').mCustomScrollbar();
  				}, 1000);
  			} else {
  				setTimeout(changeTwitter, 500);
  			}
  		}());
    }

  	if($('main').hasClass('news')) {
  		if(responsive == 'pc') {
  			$('article.list div.list').each(function(){
  				var buff = 0;
  				$(this).find('div.title ul li time').each(function() { if($(this).width() > buff) buff = $(this).width(); });
  				if(buff != 0) {
  					$(this).find('div.title ul li time').css({ 'width':buff + 40 });
  					$(this).find('div.title ul li').find('span:eq(0)').css({ 'width':$(this).width() - (buff + 40) });
  				}
  			});
  		}
  		if(responsive == 'sp') {
  			$('iframe').wrap('<div class="iframe" />')
  		}
  		$('article.detail aside.detail').share({ 'link':location.href, 'title':$('article.detail header.detail h1').text(), 'target':'tw,fl' });
  	}

  	if($('main').hasClass('profile')) {
  	}

  	if($('main').hasClass('schedule')) {
  		if(responsive == 'pc') {
  			$('article.list div.list').each(function(){
  				var buff = 0;
  				$(this).find('div.title ul li time').each(function() { if($(this).width() > buff) buff = $(this).width(); });
  				if(buff != 0) {
  					$(this).find('div.title ul li time').css({ 'width':buff + 40 });
  					$(this).find('div.title ul li').find('span:eq(0)').css({ 'width':$(this).width() - (buff + 200 + 150) });
  				}
  			});
  		}
  		if(responsive == 'sp') {
  			$('iframe').wrap('<div class="iframe" />')
  		}
  		$('article.detail aside.detail').share({ 'link':location.href, 'title':$('article.detail header.detail h1').text(), 'target':'tw,fl' });
  	}

  	if($('main').hasClass('discography')) {
  		var player_type = 'videojs';
  		if(_uac.browser == 'chrome' || _uac.browser == 'firefox') {
  			player_type = 'hls';
  			if(typeof Hls.isSupported() == 'undefined' || !Hls.isSupported()) player_type = 'videojs';
  		} else if(_uac.browser == 'safari' || _uac.browser == 'ie11') {
  			player_type = 'jplayer';
  		}
  		if(_uac.device == 'iphone' || _uac.device == 'android') player_type = 'videojs';
  		if(_uac.device == "android" && _uac.androidVer >= 4) player_type = "hls";
  		if(_uac.device == "android" && _uac.browser == "safari" && _uac.androidVer >= 4 && _uac.androidVer < 5) player_type = "videojs";
  		if(_uac.device == 'android' && _uac.androidVer < 4) player_type = 'flash';
  		$('a.player').each(function(i){
  			if(player_type == 'hls') {
  				var id = 'audio'+i;
  				$(this).append('<audio id="'+id+'"></audio>');
  				var audio = document.getElementById(id);
  				var hls = new Hls();
  				$('#'+id).closest('a').touchclick(function(e){
  					e.preventDefault();
  					var _this = this;
  					if(!$(_this).hasClass('ready')) {
  						$(_this).addClass('ready');
  						hls.loadSource('https://avex.as.smartstream.ne.jp/avexnet/_definst_/mp3:'+$(_this).attr('data-id')+'.mp3/playlist.m3u8');
  						hls.attachMedia(audio);
  						audio.play();
  						hls.on(Hls.Events.MANIFEST_PARSED,function(event, data) {
  							if(!$(_this).hasClass('on')) {
  								$('audio').each(function(){
  									this.pause();
  									this.volume = 0.5;
  									$(this).closest('a').removeClass('on');
  								});
  								audio.play();
  								$(_this).addClass('on');
  							} else {
  								audio.pause();
  								$(_this).removeClass('on');
  							}
  						});
  					} else {
  						if(!$(_this).hasClass('on')) {
  							$('audio').each(function(){
  								this.pause();
  								this.volume = 0.5;
  								$(this).closest('a').removeClass('on');
  							});
  							audio.play();
  							$(_this).addClass('on');
  						} else {
  							audio.pause();
  							$(_this).removeClass('on');
  						}
  					}
  				});
  			} else if (player_type == 'jplayer' || player_type == 'flash') {
  				var id = 'audio'+i;
  				$(this).append('<span id="'+id+'"></span>');
  				$('#'+id).closest('a').touchclick(function(e){
  					e.preventDefault();
  					var _this = this;
  					if(!$(_this).hasClass('ready')) {
  						$(_this).addClass('ready');
  						$('span', _this).jPlayer({
  							ready:function(){
  								$(this).jPlayer('setMedia', { rtmpa:'rtmp://avex.as.smartstream.ne.jp/avexnet/_definst_/mp3:'+$(_this).closest('a').attr('data-id')+'.mp3', mp3:'https://avex.as.smartstream.ne.jp/avexnet/_definst_/mp3:'+$(_this).closest('a').attr('data-id')+'.mp3/playlist.m3u8' });
  								if(!$(_this).hasClass('on')) {
  									$('span', _this).jPlayer('pauseOthers');
  									$('span', _this).jPlayer('play');
  									$('a.player').each(function(){ $(this).removeClass('on'); });
  									$(_this).addClass('on');
  								} else {
  									$('span', _this).jPlayer('pause');
  									$(_this).removeClass('on');
  								}
  							},
  							volume:0.5,
  							swfPath:'../assets/js',
  							solution:'flash,html',
  							supplied:'rtmpa,mp3'
  						});
  					} else {
  						if(!$(_this).hasClass('on')) {
  							$('span', _this).jPlayer('pauseOthers');
  							$('span', _this).jPlayer('play');
  							$('a.player').each(function(){ $(this).removeClass('on'); });
  							$(_this).addClass('on');
  						} else {
  							$('span', _this).jPlayer('pause');
  							$(_this).removeClass('on');
  						}
  					}
  				});
  			} else {
  				var id = 'audio'+i;
  				$(this).append('<audio id="'+id+'"></audio>');
  				var audio = videojs(id);
          $('#'+id).hide();
  				$('#'+id).closest('a').touchclick(function(e){
  					e.preventDefault();
  					var _this = this;
  					if(!$(_this).hasClass('ready')) {
  						$(_this).addClass('ready');
  						audio.src({ type:'application/x-mpegURL', src:'https://avex.as.smartstream.ne.jp/avexnet/_definst_/mp3:'+$(_this).closest('a').attr('data-id')+'.mp3/playlist.m3u8' });
  						if(!$(_this).hasClass('on')) {
  							$('audio').each(function(){
  								this.pause();
  								this.volume = 0.5;
  								$(this).closest('a').removeClass('on');
  							});
  							audio.play();
  							$(_this).addClass('on');
  						} else {
  							audio.pause();
  							$(_this).removeClass('on');
  						}
  					} else {
  						if(!$(_this).hasClass('on')) {
  							$('audio').each(function(){
  								this.pause();
  								this.volume = 0.5;
  								$(this).closest('a').removeClass('on');
  							});
  							audio.play();
  							$(_this).addClass('on');
  						} else {
  							audio.pause();
  							$(_this).removeClass('on');
  						}
  					}
  				});
  			}
  		});
  		if(responsive == 'sp') {
  			$('iframe').wrap('<div class="iframe" />')
  		}
  		$('article.list div.list div.thumbnail ul li').find('span:eq(0)').matchHeight();
  		$('article.detail aside.detail').each(function() {
  			if(location.href.match(/id=/)) $(this).share({ 'link':location.href, 'title':$('article.detail header.detail h1').text(), 'target':'tw,fl' });
  			else $(this).share({ 'link':location.href.substring(0, location.href.lastIndexOf('/'))+'/detail.php?id='+$(this).data('id'), 'title':$(this).closest('article.detail').find('header.detail h1').text(), 'target':'tw,fl' });
  		});
  		$('a.fancyShop').touchclick(function(e){
  			e.preventDefault();
  			if(responsive == 'pc') $.fancybox({ href:$(this).attr('href'), 'width':640, 'type':'iframe', helpers:{ overlay:{ css:{ 'background':'rgba(200,227,244,0.95)' }}} });
  			if(responsive == 'sp') $.fancybox({ href:$(this).attr('href'), 'width':'100%', 'type':'iframe', helpers:{ overlay:{ css:{ 'background':'rgba(200,227,244,0.95)' }}} });
  		});
  		$('a.fancyDownload').touchclick(function(e){
  			e.preventDefault();
  			if(responsive == 'pc') $.fancybox({ href:$(this).attr('href'), 'width':640, 'type':'iframe', helpers:{ overlay:{ css:{ 'background':'rgba(200,227,244,0.95)' }}} });
  			if(responsive == 'sp') $.fancybox({ href:$(this).attr('href'), 'width':'100%', 'type':'iframe', helpers:{ overlay:{ css:{ 'background':'rgba(200,227,244,0.95)' }}} });
  		});
  		$('aside.discography div.aside div.download ul li').find('span:eq(0)').matchHeight();
    }

  	$('nav.page div.nav ul li a.'+$('main').attr('class')).addClass('on');

  	$('nav.page div.nav aside').share({ 'link':'', 'title':'', 'target':'t,f,l' });

  	$('a').hovertouch();
  	$('button').hovertouch();

  	$('a[href^="#"]').touchclick(function(e) {
  		e.preventDefault();
  		createjs.Tween.get(document.scrollingElement, { override:true }).to({ scrollTop:$('#'+this.href.split('#')[1]).offset().top }, 500, createjs.Ease.cubicOut);
  	});

  	if(responsive == 'sp') {
    	$('nav.page header.nav button').on(touchclick, function(e){
    		e.preventDefault();
    		if(!$(this).hasClass('on')) {
    			$('nav.page div.nav').attr('data-scroll', window.pageYOffset)
    			$('html,body').addClass('on');
    			$('nav.page div.nav').addClass('on');
    			$('nav.page header.nav button').addClass('on');
    		} else {
    			$('html,body').removeClass('on');
    			$('nav.page div.nav').removeClass('on');
    			$('nav.page header.nav button').removeClass('on');
    			if($('nav.page div.nav').attr('data-scroll')) {
    				createjs.Tween.get(document.scrollingElement, { override:true }).to({ scrollTop:$('nav.page div.nav').attr('data-scroll') }, 0, createjs.Ease.cubicOut);
    				$('nav.page div.nav').attr('data-scroll', '');
    			}
    		}
    	});
  	}

  	if(responsive == 'pc') {
  		$(window).on('scroll', function(){
  			if($(window).scrollTop() <= $('nav.page').offset().top) $('nav.page div.nav section').removeClass('on');
  			else $('nav.page div.nav section').addClass('on');
  		}).trigger('scroll');
    }
  	if(responsive == 'sp') {
    	$(window).on('scroll', function() {
        if($('nav.page header.nav button').length){
      		$('nav.page header.nav button').css({ 'left':($('nav.page header.nav button').position().left == 0 ) ? -0.1:0 });
        }
    	}).trigger('scroll');
    }

  	$('div#loading').addClass('off');
	});
	loadQueue.setMaxConnections(6);
	loadQueue.loadManifest(manifest);

  if($('main').hasClass('top')){
    $('div#YTPlayer').mb_YTPlayer();
	}

});

$.fn.touchclick = function(options) {
	return this.each(function() {
		$(this).on('touchstart touchmove touchend click', function(e) {
			if(device == 'sp' && e.type == 'touchstart'){ this.is_touchclick = true; }
			if(device == 'sp' && e.type == 'touchmove'){ this.is_touchclick = false; }
			if(device == 'sp' && e.type == 'touchend' && this.is_touchclick){ this.is_touchclick = false; return options.call(this, e); }
			if(device == 'sp' && e.type == 'click'){ e.preventDefault(); }
			if(device == 'pc' && e.type == 'click'){ return options.call(this, e); }
		})
	});
};

$.fn.hovertouch = function(options) {
	this.each(function() {
		$(this).on('touchstart touchmove touchend mouseenter mouseleave', function(e) {
			if(device == 'sp' && e.type == 'touchstart'){ this.is_hovertouch = true; }
			if(device == 'sp' && e.type == 'touchmove'){ this.is_hovertouch = false; }
			if(device == 'sp' && e.type == 'touchend' && this.is_hovertouch){ this.is_hovertouch = false; e.currentTarget.classList.add('touch'); }
			if(device == 'pc' && e.type == 'mouseenter'){ e.currentTarget.classList.add('hover'); }
			if(device == 'pc' && e.type == 'mouseleave'){ e.currentTarget.classList.remove('hover'); }
		})
	});
};

$.fn.share = function(options){
	var hash = '洛天依,LuoTianyi,VOCALOID';

	var array = options.target.split(',');
	var path = ($('main').hasClass('top')) ? './' : '../';
	var html = '';
	html += '<ul>';
	$.each(array, function(i, value) {
		if(value == 't') html += '<li><a href="http://twitter.com/share?text='+ encodeURIComponent(options.title) +'&url=' + encodeURIComponent(options.link) + '&hashtags='+hash+'" onclick="window.open(this.href, \'TWwindow\', \'width=550, height=480, menubar=no, toolbar=no, scrollbars=yes\'); return false;" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" class="twitter" width="350px" height="300px" viewBox="0 0 350 300"><defs></defs><path class="fill" d="M350.001,35.509 C346.026,42.167 340.649,49.197 333.870,56.595 C328.493,62.513 321.944,68.556 314.231,74.720 C314.231,74.720 314.231,76.940 314.231,76.940 C314.231,76.940 314.231,79.530 314.231,79.530 C314.231,80.762 314.346,81.626 314.579,82.119 C314.579,82.119 314.579,84.708 314.579,84.708 C314.579,110.109 310.022,135.572 300.903,161.097 C291.785,186.620 278.809,209.494 261.975,229.715 C243.971,251.417 222.113,268.556 196.394,281.134 C170.674,293.711 141.917,299.999 110.122,299.999 C89.546,299.999 70.142,297.041 51.904,291.122 C33.201,285.202 15.899,276.818 -0.001,265.967 C0.936,266.214 2.337,266.338 4.208,266.338 C7.948,266.831 10.755,267.077 12.626,267.077 C12.626,267.077 17.183,267.077 17.183,267.077 C33.550,267.077 49.567,264.242 65.231,258.569 C79.727,253.144 93.403,245.253 106.263,234.895 C91.300,234.649 77.387,229.469 64.531,219.357 C51.904,209.494 43.486,197.040 39.279,181.997 C42.786,182.737 45.007,183.105 45.943,183.105 C45.943,183.105 49.447,183.105 49.447,183.105 C50.151,183.352 51.202,183.476 52.605,183.476 C54.708,183.476 56.346,183.352 57.516,183.105 C59.853,183.105 63.128,182.612 67.335,181.626 C67.801,181.626 68.505,181.502 69.439,181.256 C70.376,181.009 71.075,180.887 71.542,180.887 C54.941,177.434 41.265,168.679 30.509,154.622 C19.520,140.565 14.029,124.536 14.029,106.534 C14.029,106.534 14.029,106.163 14.029,106.163 C14.029,106.163 14.029,105.794 14.029,105.794 C14.029,105.794 14.029,105.424 14.029,105.424 C18.471,108.383 23.615,110.603 29.460,112.082 C35.538,114.054 41.265,115.042 46.644,115.042 C36.354,107.644 28.640,98.642 23.497,88.038 C17.651,77.187 14.729,65.102 14.729,51.786 C14.729,44.388 15.546,37.729 17.183,31.810 C18.120,27.617 20.457,21.576 24.198,13.685 C42.435,37.358 64.177,55.854 89.429,69.172 C115.382,83.475 142.969,91.366 172.195,92.847 C171.494,87.667 171.145,84.832 171.145,84.339 C170.674,80.886 170.441,78.051 170.441,75.830 C170.441,54.868 177.456,36.989 191.483,22.193 C205.512,7.396 222.462,-0.002 242.337,-0.002 C252.623,-0.002 262.325,2.094 271.444,6.286 C280.562,10.971 288.394,16.891 294.942,24.042 C302.423,22.315 310.372,19.850 318.788,16.644 C325.803,13.931 333.051,10.232 340.532,5.547 C337.729,14.424 333.634,22.439 328.260,29.591 C322.179,36.989 315.751,42.907 308.969,47.347 C315.984,46.113 322.999,44.634 330.010,42.907 C335.388,41.428 342.052,38.961 350.001,35.509 Z"></svg></a></li>';
		if(value == 'f') html += '<li><a href="http://www.facebook.com/share.php?u='+encodeURIComponent(options.link)+'" onclick="window.open(this.href, \'FBwindow\', \'width=650, height=450, menubar=no, toolbar=no, scrollbars=yes\'); return false;" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" class="facebook" width="156px" height="300px" viewBox="0 0 156 300"><defs></defs><path class="fill" d="M101.000,300.000 C101.000,300.000 101.000,163.000 101.000,163.000 C101.000,163.000 147.000,163.000 147.000,163.000 C147.000,163.000 154.000,110.000 154.000,110.000 C154.000,110.000 101.000,110.000 101.000,110.000 C101.000,110.000 101.000,76.000 101.000,76.000 C101.000,60.552 105.857,50.000 128.000,50.000 C128.000,50.000 156.000,50.000 156.000,50.000 C156.000,50.000 156.000,2.000 156.000,2.000 C151.113,1.351 134.503,-0.000 115.000,-0.000 C74.282,-0.000 46.000,25.336 46.000,71.000 C46.000,71.000 46.000,110.000 46.000,110.000 C46.000,110.000 0.000,110.000 0.000,110.000 C0.000,110.000 0.000,163.000 0.000,163.000 C0.000,163.000 46.000,163.000 46.000,163.000 C46.000,163.000 46.000,300.000 46.000,300.000 C46.000,300.000 101.000,300.000 101.000,300.000 Z"></svg></a></li>';
		if(value == 'l') html += '<li><a href="http://line.me/R/msg/text/?'+options.title+'%0d%0a'+encodeURIComponent(options.link)+'"><svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" class="line" width="315px" height="300px" viewBox="0 0 315 300"><defs></defs><path class="fill" d="M280.344,206.351 C280.344,206.351 280.354,206.351 280.354,206.351 C247.419,244.375 173.764,290.686 157.006,297.764 C140.251,304.844 142.724,293.258 143.409,289.286 C143.809,286.909 145.648,275.795 145.648,275.795 C146.179,271.773 146.725,265.543 145.139,261.573 C143.374,257.197 136.418,254.902 131.307,253.804 C55.860,243.805 0.004,190.897 0.004,127.748 C0.004,57.307 70.443,-0.006 157.006,-0.006 C243.579,-0.006 314.004,57.307 314.004,127.748 C314.004,155.946 303.108,181.342 280.344,206.351 ZM95.547,153.146 C95.547,153.146 72.581,153.146 72.581,153.146 C72.581,153.146 72.581,98.841 72.581,98.841 C72.581,94.296 68.894,90.583 64.352,90.583 C59.819,90.583 56.127,94.296 56.127,98.841 C56.127,98.841 56.127,161.398 56.127,161.398 C56.127,165.960 59.819,169.660 64.352,169.660 C64.352,169.660 95.547,169.660 95.547,169.660 C100.092,169.660 103.777,165.960 103.777,161.398 C103.777,156.851 100.092,153.146 95.547,153.146 ZM127.810,98.841 C127.810,94.296 124.120,90.583 119.583,90.583 C115.046,90.583 111.356,94.296 111.356,98.841 C111.356,98.841 111.356,161.398 111.356,161.398 C111.356,165.960 115.046,169.660 119.583,169.660 C124.120,169.660 127.810,165.960 127.810,161.398 C127.810,161.398 127.810,98.841 127.810,98.841 ZM202.908,98.841 C202.908,94.296 199.219,90.583 194.676,90.583 C190.137,90.583 186.442,94.296 186.442,98.841 C186.442,98.841 186.442,137.559 186.442,137.559 C186.442,137.559 154.466,93.894 154.466,93.894 C152.926,91.818 150.460,90.583 147.892,90.583 C147.007,90.583 146.127,90.730 145.282,91.010 C141.916,92.142 139.650,95.287 139.650,98.841 C139.650,98.841 139.650,161.398 139.650,161.398 C139.650,165.960 143.345,169.660 147.885,169.660 C152.427,169.660 156.114,165.960 156.114,161.398 C156.114,161.398 156.114,122.705 156.114,122.705 C156.114,122.705 188.090,166.354 188.090,166.354 C189.637,168.431 192.094,169.660 194.667,169.660 C195.546,169.660 196.434,169.521 197.279,169.236 C200.650,168.114 202.908,164.966 202.908,161.398 C202.908,161.398 202.908,98.841 202.908,98.841 ZM253.385,138.381 C257.927,138.381 261.617,134.674 261.617,130.129 C261.617,125.569 257.927,121.872 253.385,121.872 C253.385,121.872 230.426,121.872 230.426,121.872 C230.426,121.872 230.426,107.103 230.426,107.103 C230.426,107.103 253.385,107.103 253.385,107.103 C257.927,107.103 261.617,103.398 261.617,98.841 C261.617,94.296 257.927,90.583 253.385,90.583 C253.385,90.583 222.187,90.583 222.187,90.583 C217.650,90.583 213.955,94.296 213.955,98.841 C213.955,98.850 213.955,98.858 213.955,98.878 C213.955,98.878 213.955,130.109 213.955,130.109 C213.955,130.114 213.955,130.129 213.955,130.129 C213.955,130.139 213.955,130.139 213.955,130.149 C213.955,130.149 213.955,161.398 213.955,161.398 C213.955,165.960 217.655,169.660 222.187,169.660 C222.187,169.660 253.385,169.660 253.385,169.660 C257.915,169.660 261.617,165.960 261.617,161.398 C261.617,156.851 257.915,153.146 253.385,153.146 C253.385,153.146 230.426,153.146 230.426,153.146 C230.426,153.146 230.426,138.381 230.426,138.381 C230.426,138.381 253.385,138.381 253.385,138.381 Z"></svg></a></li>';
		if(value == 'tw') html += '<li><a href="http://twitter.com/share" class="twitter-share-button" data-text="'+options.title+'" data-url="'+options.link+'" data-counturl="'+options.link+'" data-hashtags="'+hash+'" data-count="none" data-lang="ja">Tweet</a><script type="text/javascript" src="http://platform.twitter.com/widgets.js" charset="utf-8"></script></li>';
		if(value == 'fl') html += '<li><script>(function(d, s, id) { var js, fjs = d.getElementsByTagName(s)[0]; if (d.getElementById(id)) return; js = d.createElement(s); js.id = id; js.src = "//connect.facebook.net/ja_JP/sdk.js#xfbml=1&version=v2.0"; fjs.parentNode.insertBefore(js, fjs); }(document, \'script\', \'facebook-jssdk\'));</script><div class="fb-like" data-href="'+options.link+'" data-layout="button_count"></div></li>';
	});
	html += '</ul>';
	$(this).append(html);
};
