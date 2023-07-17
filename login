<!DOCTYPE html>
<html>
<head>
  <title>Login Form with Particle.js Background</title>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bootstrap/5.3.0/css/bootstrap.min.css">
  <style>
    body {
      background-color: #f8f9fa;
      overflow: hidden;
    }

    #particle-container {
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      z-index: -1;
    }

    .login-container {
      position: relative;
      z-index: 1;
      max-width: 400px;
      margin: 0 auto;
      margin-top: 150px;
      padding: 20px;
      background-color: rgba(255, 255, 255, 0.8);
      border-radius: 5px;
      box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    }

    .login-container h2 {
      text-align: center;
      margin-bottom: 20px;
      color: #ff8c00;
    }

    .form-group {
      margin-bottom: 20px;
    }

    .form-group label {
      font-weight: bold;
    }

    .form-group input[type="text"],
    .form-group input[type="password"] {
      width: 100%;
      padding: 10px;
      font-size: 16px;
      border: 1px solid #ddd;
      border-radius: 5px;
    }

    .form-group input[type="submit"] {
      width: 100%;
      padding: 10px;
      font-size: 16px;
      background-color: #ff8c00;
      color: #fff;
      border: none;
      border-radius: 5px;
      cursor: pointer;
    }

    .form-group input[type="submit"].loading {
      background-color: #ff6600;
      cursor: not-allowed;
    }

    .form-group input[type="submit"]:hover {
      background-color: #ff6600;
    }

    .form-group .text-center {
      margin-top: 10px;
    }

    .form-group .text-center a {
      color: #ff8c00;
      text-decoration: none;
    }
  </style>
</head>
<body>
  <div id="particle-container"></div>
  <div class="container">
    <div class="row">
      <div class="col-md-6 offset-md-3">
        <div class="login-container">
          <h2>Login</h2>
          <form id="login-form">
            <div class="form-group">
              <label for="username">Username</label>
              <input type="text" id="username" placeholder="Enter your username">
            </div>
            <div class="form-group">
              <label for="password">Password</label>
              <input type="password" id="password" placeholder="Enter your password">
            </div>
            <div class="form-group">
              <input type="submit" value="Login" id="login-button">
            </div>
            <div class="form-group text-center">
              <a href="#">Forgot password?</a>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>

  <script src="https://cdnjs.cloudflare.com/ajax/libs/particles.js/2.0.0/particles.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
  <script>
    particlesJS("particle-container", {
      particles: {
        number: {
          value: 80,
          density: {
            enable: true,
            value_area: 800
          }
        },
        color: {
          value: "#ff8c00"
        },
        shape: {
          type: "circle",
          stroke: {
            width: 0,
            color: "#000000"
          },
          polygon: {
            nb_sides: 5
          },
          image: {
            src: "img/github.svg",
            width: 100,
            height: 100
          }
        },
        opacity: {
          value: 0.5,
          random: false,
          anim: {
            enable: false,
            speed: 1,
            opacity_min: 0.1,
            sync: false
          }
        },
        size: {
          value: 3,
          random: true,
          anim: {
            enable: false,
            speed: 40,
            size_min: 0.1,
            sync: false
          }
        },
        line_linked: {
          enable: true,
          distance: 150,
          color: "#ff8c00",
          opacity: 0.4,
          width: 1
        },
        move: {
          enable: true,
          speed: 6,
          direction: "none",
          random: false,
          straight: false,
          out_mode: "out",
          bounce: false,
          attract: {
            enable: false,
            rotateX: 600,
            rotateY: 1200
          }
        }
      },
      interactivity: {
        detect_on: "canvas",
        events: {
          onhover: {
            enable: true,
            mode: "repulse"
          },
          onclick: {
            enable: true,
            mode: "push"
          },
          resize: true
        },
        modes: {
          grab: {
            distance: 400,
            line_linked: {
              opacity: 1
            }
          },
          bubble: {
            distance: 400,
            size: 40,
            duration: 2,
            opacity: 8,
            speed: 3
          },
          repulse: {
            distance: 200,
            duration: 0.4
          },
          push: {
            particles_nb: 4
          },
          remove: {
            particles_nb: 2
          }
        }
      },
      retina_detect: true
    });

    $(document).ready(function() {
      const loginForm = $('#login-form');
      const loginButton = $('#login-button');

      loginForm.on('submit', function(event) {
        event.preventDefault();

        const username = $('#username').val();
        const password = $('#password').val();

        if (username && password) {
          loginButton.prop('disabled', true);
          loginButton.val('Logging in...');

          // Simulate login request
          setTimeout(function() {
            // Perform actual login logic
            // ...

            // On success, redirect or display success message
            alert('Login successful');
          }, 2000);
        } else {
          alert('Invalid username or password');
        }
      });
    });
  </script>
</body>
</html>
