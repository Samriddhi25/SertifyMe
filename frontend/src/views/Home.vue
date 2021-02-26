<template>
  <main-layout>
    <div class="block">
      <div class="block-left">
        <img src="../assets/1.png" class="photo_image" />
      </div>
      <div class="block-right">
        <div class="heading">About Us</div>
        <div class="content">
          SertifyMe is a Web application which provides a simple solution to the
          tedious task of publishing and distributing e-certificates. It allows
          you to issue electronic business cards, ID badges, certificates and
          other such artefacts in a quick and hassle free manner. Furthermore,
          SertifyMe works with your existing security infrastructure and
          workflow; it does not require any additional software or special
          integration. In fact, integrating SertifyMe into your corporate IT
          environment is as simple as copying two files to a web server on the
          internet.
        </div>
      </div>
    </div>
    <div class="block-mid">
      <div class="block-left">
        <div class="heading">Services We Provide</div>
        <div class="sub-heading">Automated Email</div>
        <div class="sub-content">
          This feature enable the user or the organization to automatically send
          the generated certificate via e-mail.
        </div>
        <div class="sub-heading">Hardware Independent</div>
        <div class="sub-content">
          Prevents you from running out of system requirements since it is a web
          based application.
        </div>
        <div class="sub-heading">Personalization</div>
        <div class="sub-content">
          It lets you choose certificate template as per your wish. You can
          provide custom data to be processed.
        </div>
      </div>
      <div class="block-right">
        <img src="../assets/2.png" class="photo_image" />
      </div>
    </div>
    <div class="block">
      <div class="block-left">
        <img src="../assets/3.png" class="photo_image" />
      </div>
      <div class="block-right">
        <div class="heading">Contact Us</div>
        <div class="content">
          If you have any query, please feel free to drop me a note. If you
          don't get an answer immediately, I might just be travelling through
          the middle of nowhere. I'll get back to you as soon as I can.
          <div class="Feedback-modal">
            <a
              href="/#login"
              @click.prevent="show"
              class="Feeback-btn"
              >Write To Us</a>
            <modal
              name="modal-login"
              @opened="opened"
              :adaptive="true"
              :height="440"
              :width="580"
            >
                <ContactForm />
            </modal>
          </div>
        </div>
      </div>
    </div>
  </main-layout>
</template>

<script>
import MainLayout from "../components/layout/Main";
import ContactForm from "../components/layout/ContactForm";

export default {
  components: {
    MainLayout,
    ContactForm,
  },
  methods: {
    show() {
      this.$modal.show("modal-login");
    },
    opened() {
      this.$refs.email.focus();
    },
    hide() {
      this.$modal.hide("modal-login");
    },
  },
};
</script>

<style scoped>
.block {
  display: flex;
  flex-direction: row;
  width: 100vw;
  height: 450px;
}
.block-mid {
  display: flex;
  flex-direction: row;
  width: 100vw;
  padding-left: 30px;
  height: 500px;
}
.block-left {
  width: 50vw;
}
.block-right {
  width: 50vw;
}
.heading {
  font-size: 42px;
  margin: 20px;
  margin-top: 50px;
  font-weight: bolder;
  color: #0d1413;
}
.sub-heading {
  font-size: 22px;
  margin: 5px;
  text-decoration: underline;
  padding-left: 40px;
  font-weight: bold;
  color: #001716;
}
.content {
  font-size: 16px;
  margin: 40px;
  line-height: 30px;
  margin-left: 20px;
  margin-top: 0;
}
.sub-content {
  font-size: 16px;
  margin: 40px;
  line-height: 15px;
  margin-left: 45px;
  margin-top: 0;
}
.photo_image {
  height: 100%;
  padding-left: 150px;
}
.Feeback-btn {
  color: #4A8280;
  padding: 10px 30px;
  border: 1px solid #4A8280;
  background-color: #0d1413;
  border-radius: 32.33px;
  text-decoration: none;
  font-weight: bold;
}
.Feeback-btn:hover {
  color: #0d1413;
  border: 1px solid #0d1413;
  background-color: #4A8280;
}
.Feedback-modal {
  margin-top: 50px;
}
</style>

