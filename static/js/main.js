document.addEventListener('DOMContentLoaded', () => {
  "use strict";

  /**
   * Preloader
   */
  const preloader = document.querySelector('#preloader');
  if (preloader) {
    window.addEventListener('load', () => {
      preloader.remove();
    });
  }

  /**
   * Mobile nav toggle
   */

  const mobileNavShow = document.querySelector('.mobile-nav-show');
  const mobileNavHide = document.querySelector('.mobile-nav-hide');

  document.querySelectorAll('.mobile-nav-toggle').forEach(el => {
    el.addEventListener('click', function (event) {
      event.preventDefault();
      mobileNavToogle();
    });
  });

  function mobileNavToogle() {
    document.querySelector('body').classList.toggle('mobile-nav-active');
    mobileNavShow.classList.toggle('d-none');
    mobileNavHide.classList.toggle('d-none');
  }

  /**
   * Hide mobile nav on same-page/hash links
   */
  document.querySelectorAll('#navbar a').forEach(navbarlink => {

    if (!navbarlink.hash) return;

    let section = document.querySelector(navbarlink.hash);
    if (!section) return;

    navbarlink.addEventListener('click', () => {
      if (document.querySelector('.mobile-nav-active')) {
        mobileNavToogle();
      }
    });

  });

  /**
   * Toggle mobile nav dropdowns
   */
  const navDropdowns = document.querySelectorAll('.navbar .dropdown > a');

  navDropdowns.forEach(el => {
    el.addEventListener('click', function (event) {
      if (document.querySelector('.mobile-nav-active')) {
        event.preventDefault();
        this.classList.toggle('active');
        this.nextElementSibling.classList.toggle('dropdown-active');

        let dropDownIndicator = this.querySelector('.dropdown-indicator');
        dropDownIndicator.classList.toggle('bi-chevron-up');
        dropDownIndicator.classList.toggle('bi-chevron-down');
      }
    });
  });

  /**
   * Scroll top button
   */
  const scrollTop = document.querySelector('.scroll-top');
  if (scrollTop) {
    const togglescrollTop = function () {
  		if (window.scrollY > 100) 
  			scrollTop.classList.add('active');
  		else
  			scrollTop.classList.remove('active');
    };
    window.addEventListener('load', togglescrollTop);
    document.addEventListener('scroll', togglescrollTop);
    scrollTop.addEventListener('click', window.scrollTo({
      top: 0,
      behavior: 'smooth'
    }));
  }


  /**
   * Init swiper slider with 1 slide at once in desktop view
   */
  new Swiper('.slides-1', {
    speed: 600,
    loop: true,
    autoplay: {
      delay: 5000,
      disableOnInteraction: false
    },
    slidesPerView: 'auto',
    pagination: {
      el: '.swiper-pagination',
      type: 'bullets',
      clickable: true
    },
    navigation: {
      nextEl: '.swiper-button-next',
      prevEl: '.swiper-button-prev',
    }
  });

  /**
   * Init swiper slider with 2 slides at once in desktop view
   */
  new Swiper('.slides-2', {
    speed: 600,
    loop: true,
    autoplay: {
      delay: 5000,
      disableOnInteraction: false
    },
    slidesPerView: 'auto',
    pagination: {
      el: '.swiper-pagination',
      type: 'bullets',
      clickable: true
    },
    navigation: {
      nextEl: '.swiper-button-next',
      prevEl: '.swiper-button-prev',
    },
    breakpoints: {
      320: {
        slidesPerView: 1,
        spaceBetween: 20
      },

      1200: {
        slidesPerView: 2,
        spaceBetween: 20
      }
    }
  });

  /**
   * Animation on scroll function and init
   */
  function aos_init() {
    AOS.init({
      duration: 800,
      easing: 'slide',
      once: true,
      mirror: false
    });
  }
  window.addEventListener('load', () => {
    aos_init();
  });

  // Below is the javascript that I wrote for the project

  // Get the modal element
  var modal = document.getElementById("myModal");

  // Get the links that open the modal
  var linkA = document.getElementById("PP");
  var linkB = document.getElementById("TOS");

  // Get the close button element
  var closeButton = document.getElementsByClassName("close")[0];

  // Get the modal content elements
  var modalTitle = document.getElementById("modalTitle");
  var modalContent = document.getElementById("modalContent");

  // Open the modal with content for TOS
  linkA.onclick = function () {
    modalTitle.textContent = "Privacy Policy";
    modalContent.innerHTML = `
    <h3>Effective Date: 2020-01-01</h3>

    <p>This Privacy Policy describes how EnigmaMachine ("we," "us," or "our") collects, uses, discloses, and safeguards personal information of users ("you" or "users") who visit our website and engage with our services. This policy applies to the information collected by EnigmaMachine both online and offline.</p>

    <h3>Information We Collect:</h3>

    <p>Personal Information: We may collect personal information such as your name, email address, phone number, and any other information you provide voluntarily when you interact with us or use our services.</p>
    <p>Usage Information: We collect non-personal information about your interactions with our website and services, including IP address, browser type, device information, pages visited, and other similar data.</p>

    <h3>Use of Collected Information:</h3>

    <p>We may use the collected information to provide, maintain, and improve our services, personalize user experience, respond to inquiries, send notifications, and fulfill user requests.</p>
    <p>We may also use the information to analyze trends, monitor the effectiveness of our marketing campaigns, and prevent fraudulent or unauthorized activities.</p>

    <h3>Information Sharing:</h3>

    <p>We do not sell, trade, or rent your personal information to third parties without your explicit consent, except as described in this Privacy Policy.</p>
    <p>We may share personal information with trusted service providers who assist us in operating our website, conducting business activities, or servicing users, subject to confidentiality agreements.</p>
    <p>We may disclose personal information if required by law, to protect our rights, or to comply with legal processes.</p>

    <h3>Data Security:</h3>

    <p>We take reasonable precautions to protect the security of your personal information. However, no method of transmission or electronic storage is completely secure, and we cannot guarantee absolute security.</p>
    <p>We implement appropriate technical and organizational measures to safeguard your personal information and regularly review and enhance our security practices.</p>

    <h3>Cookies and Tracking Technologies:</h3>

    <p>We may use cookies, web beacons, and similar tracking technologies to enhance user experience, analyze website usage, and provide personalized content.</p>
    <p>You have the option to disable cookies through your browser settings; however, this may affect your ability to access certain features of our website.</p>

    <h3>Third-Party Websites:</h3>

    <p>Our website may contain links to third-party websites or services that are not owned or controlled by us. This Privacy Policy does not apply to those websites, and we are not responsible for their practices. We encourage you to review the privacy policies of such third parties.</p>

    <h3>Children's Privacy:</h3>

    <p>Our website and services are not intended for individuals under the age of 18. We do not knowingly collect or solicit personal information from children. If we discover that we have collected personal information from a child, we will promptly delete it.</p>

    <h3>Your Privacy Choices and Rights:</h3>

    <p>You have the right to access, correct, or delete your personal information in accordance with applicable laws. You may also have the right to object to or restrict certain processing activities.</p>
    <p>To exercise your rights or for any privacy-related inquiries, please contact us using the information provided below.</p>

    <h3>Changes to this Privacy Policy:</h3>

    <p>We reserve the right to modify or update this Privacy Policy at any time. We will notify you of any material changes by posting the updated policy on our website or through other appropriate communication channels.</p>

    <h3>Contact Us:</h3>

    <p>If you have any questions, concerns, or requests regarding this Privacy Policy or our privacy practices, please contact us at [Insert contact information].</p>

    <p>By accessing or using our website and services, you acknowledge that you have read and understood this Privacy Policy and agree to the collection, use, and disclosure of your personal information as described herein.</p>
  `;

    modal.style.display = "block";
  };

  // Open the modal with content for Link B
  linkB.onclick = function () {
    modalTitle.textContent = "Terms of Service";
    modalContent.innerHTML = `
  <p>These Terms of Service ("Terms") govern your use of our escape room services and website. By booking an escape room experience with us or using our website, you agree to abide by these Terms. Please read them carefully.</p>

  <h3>Booking and Participation:</h3>
  <ol>
    <li>Participants must be at least 18 years old or accompanied by a responsible adult.</li>
    <li>Bookings can be made through our website, phone, or in person. All bookings are subject to availability.</li>
    <li>Participants must arrive at the designated time for their booking. Late arrivals may result in reduced game time.</li>
    <li>Participants agree to follow all instructions provided by Enigma Machine staff and adhere to the rules and regulations of the escape room experience.</li>
  </ol>

  <h3>Code of Conduct:</h3>
  <ol>
    <li>Participants must treat Enigma Machine staff and fellow participants with respect and refrain from engaging in any form of harassment, discrimination, or disruptive behavior.</li>
    <li>Participants must not disclose or share any confidential information, puzzles, or solutions related to the escape room experience.</li>
    <li>Participants are responsible for the care and preservation of the escape room facilities and props. Any intentional damage caused may result in liability for repair or replacement costs.</li>
  </ol>

  <h3>Safety:</h3>
  <ol>
    <li>Participants must follow all safety guidelines provided by Enigma Machine staff.</li>
    <li>Participants with known medical conditions or who are pregnant should consult with a medical professional before participating.</li>
    <li>Participants must not use excessive force, climb on furniture or fixtures, or engage in any unsafe behavior during the escape room experience.</li>
  </ol>

  <h3>Intellectual Property:</h3>
  <ol>
    <li>Enigma Machine retains all intellectual property rights related to the escape room experience, including but not limited to puzzles, designs, and logos.</li>
    <li>Participants must not reproduce, distribute, or use any Enigma Machine intellectual property without prior written consent.</li>
  </ol>

  <h3>Liability:</h3>
  <ol>
    <li>Participants acknowledge that the escape room experience may involve physical exertion, mental challenges, and potential risks. Participation is voluntary, and participants assume all risks associated with their involvement.</li>
    <li>Enigma Machine is not liable for any personal injury, loss, or damage to personal property that may occur during the escape room experience, except in cases of gross negligence or willful misconduct.</li>
  </ol>

  <h3>Privacy:</h3>
  <ol>
    <li>Enigma Machine respects your privacy and handles personal information in accordance with applicable privacy laws and our Privacy Policy.</li>
    <li>By participating in our escape room experience or using our website, you consent to the collection, use, and processing of your personal information as described in our Privacy Policy.</li>
  </ol>

  <h3>Modifications and Cancellations:</h3>
  <p>Enigma Machine reserves the right to modify, cancel, or reschedule bookings or events due to unforeseen circumstances. We will make reasonable efforts to notify affected participants in advance.</p>

  <h3>Governing Law and Jurisdiction:</h3>
  <p>These Terms shall be governed by and construed in accordance with the laws of Sweden. Any disputes arising under these Terms shall be subject to the exclusive jurisdiction of the courts in Sweden.</p>

  <h3>Severability:</h3>
  <p>If any provision of these Terms is found to be invalid or unenforceable, the remaining provisions shall continue to be valid and enforceable to the fullest extent permitted by law.</p>

  <h3>Contact Us:</h3>
  <p>If you have any questions or concerns regarding these Terms, please contact us using the information provided on our website.</p>

  <p>By participating in the escape room experience or using our website, you acknowledge that you have read, understood, and agreed to these Terms of Service.</p>
`;

    modal.style.display = "block";
  };

  // Close the modal when the close button is clicked
  closeButton.onclick = function () {
    modal.style.display = "none";
  };

  // Close the modal when clicking outside the modal content
  window.onclick = function (event) {
    if (event.target == modal) {
      modal.style.display = "none";
    }
  };

});