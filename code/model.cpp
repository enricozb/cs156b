/* 
 * "Model" class provides an abstract framework to guide implementations
 * of specific models. Currently, this is a  "pure abstract class," 
 * meaning it exclusively has pure virtual functions (and no data).
 * Feel free to change that, if you need.
 */


class Model {

/* Accessible from anywhere where the object is visible. */
public:

   /* Pure virtual functions providing interface framework. */
   virtual int train() = 0;
   virtual int predict() = 0;
   virtual int serialize() = 0;
   virtual int deserialize() = 0;

/* Accessible from other members of the same class, but also from members of their derived classes. */
protected:

/* Accessible only from within other members of the same class (or from their "friends"). */
private:


};