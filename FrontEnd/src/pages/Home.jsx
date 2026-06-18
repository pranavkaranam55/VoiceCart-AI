import HeroSection from "../components/HeroSection";
import FeatureCard from "../components/FeatureCard";
import VoiceRecorder from "../components/VoiceRecorder";
import Footer from "../components/Footer";

function Home() {
  return (
    <div>

      <HeroSection />

      <VoiceRecorder />

      <section className="features-section">

        <FeatureCard
          title="Multilingual Support"
          description="Supports multiple languages for diverse customers."
        />

        <FeatureCard
          title="AI Speech Recognition"
          description="Transforms speech into structured orders instantly."
        />

        <FeatureCard
          title="Real-Time Processing"
          description="Processes orders quickly with minimal delay."
        />

        <FeatureCard
title="Enterprise Grade Security"
          description="Built with enterprise-grade reliability."
        />

      </section>
      <Footer />
    </div>
  );
}

export default Home;